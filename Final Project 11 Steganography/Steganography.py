#! /bin/usr/env python3.4

import numpy as np
import scipy
import PIL
from imageio import *
import base64
import re
import copy
import zlib
from os.path import join
import sys

class Payload():
    def __init__(self, rawData=None, compressionLevel=-1, json=None):
        if rawData is not None and json is None:
            if isinstance(rawData, np.ndarray):
                if compressionLevel > 9 or compressionLevel < -1:
                    raise ValueError("compressionLevel must be between -1 and 9")
                elif compressionLevel >= -1 and compressionLevel <= 9:
                    self.rawData = rawData
                    crd = self.compressData(compressionLevel) #compressed rawData
                    b64rd = self.convert2Base64(crd) #base64 rawData format
                    if len(list(self.rawData.shape)) == 1:
                        ttype = "text"
                    elif len(list(self.rawData.shape)) == 2:
                        ttype = "gray"
                    elif len(list(self.rawData.shape)) == 3:
                        ttype = "color"
                    if len(list(self.rawData.shape)) == 2 or len(list(self.rawData.shape)) == 3:
                        trow = list(self.rawData.shape)[0]
                        tcol = list(self.rawData.shape)[1]
                    if compressionLevel == -1:
                        isComp = "false"
                    else: #compressionLevel <= 9 and compressionLevel >= 0:
                        isComp = "true"
                    tjson = "{"
                    if ttype == "text":
                        tjson = tjson + '"type":"text","size":null,"isCompressed":{0},"content":"{1}"'.format(isComp,str(b64rd)[2:-1])
                    else:
                        tjson = tjson + '"type":"{0}","size":"{1},{2}","isCompressed":{3},"content":"{4}"'.format(ttype, trow,tcol, isComp, str(b64rd)[2:-1])
                    tjson = tjson + "}"
                    self.json = tjson.strip()
            else:
                 raise TypeError("rawData input is an incorrect type")
        elif json is not None:
            if type(json) is not str:
                raise TypeError("json input is an incorrect type")
            else:
                self.json = json
                temp = self.constructRD()
                self.rawData = np.frombuffer(temp,dtype=np.uint8)
                self.rawData = self.constructRD()
        else:
            raise ValueError("invalid rawData and json inputs")

    def compressData(self,compressionLevel):
        arr1D = self.rasterScan()
        if compressionLevel == -1:
            return arr1D
        else:
            compressedBytes = zlib.compress(arr1D, compressionLevel)
            compressedArr = np.frombuffer(compressedBytes,dtype=np.uint8)
            return compressedArr

    def rasterScan(self):
        templ = list(self.rawData.shape)
        if len(templ) == 2 or len(templ) == 1: #if it is gray or text
            return self.rawData.flatten()
        elif len(templ) == 3: #if it is color
            temp = []
            for x in self.rawData:
                for y in x:
                    temp.append(y[0]) #red channel
                    temp.append(y[1]) #green channel
                    temp.append(y[2]) #blue channel
            pixels = np.asarray(temp)
            return pixels

    def convert2Base64(self, crd):
        return base64.b64encode(crd)

    def constructRD(self):
        expr = r"^\{\"type\":\"(?P<type>[\w]+)\",\"size\":(?P<size>.*)\,\"isCompressed\":(?P<isC>[\w]+),\"content\":\"(?P<content>.*)\"\}$"
        m = re.match(expr,self.json)
        ttype = m.group("type")
        tsize = m.group("size")
        tisC = m.group("isC")
        tbcnt = m.group("content")
        db64 = base64.b64decode(tbcnt)
        if tisC == "true":
            res = list(zlib.decompress(db64))
        else:
            res = list(db64)
        if ttype == "gray":
            trow = tsize.split(",")[0][1:]
            tcol = tsize.split(",")[1][:-1]
            grd = np.array(res,dtype=(np.uint8)).reshape(int(trow), int(tcol))
            return grd
        elif ttype == "color":
            tlen = int(len(res)/3)
            trow = tsize.split(",")[0][1:]
            tcol = tsize.split(",")[1][:-1]
            grd = np.asarray([[res[i], res[i+tlen], res[i+2*tlen]] for i in range(tlen)],dtype=(np.uint8)).transpose().reshape(int(trow),int(tcol), 3)
            return grd
        else: #if json is text
            grd = np.asarray(res,dtype=(np.uint8))
            return grd

class Carrier(object):
    def __init__(self, img):
        if img is not None:
            if isinstance(img,np.ndarray):
                self.img = img
                if len(img.shape) >= 3:
                    if img.shape[len(img.shape) - 1] >= 4:
                        self.nrows = list(self.img.shape)[0]
                        self.ncols = list(self.img.shape)[1]
                    else:
                        raise ValueError("img contains less than 4 dimensions")
                else:
                    raise ValueError("img contains less than 3 dimensions")
            else:
                raise TypeError("img is an incorrect type")

    def payloadExists(self):
        string = "{\"type\":"
        tlist = []
        imgc = np.copy(self.img)
        for x in range(1):#self.img: #first row of pixels
            if (len(imgc[x])) < 8:
                return False
            for y in range(8): #range(8):
                temp = []
                a8b = "{0:08b}".format(imgc[x][y][3])
                temp.append(a8b[-2:])
                b8b = "{0:08b}".format(imgc[x][y][2])
                temp.append(b8b[-2:])
                g8b = "{0:08b}".format(imgc[x][y][1])
                temp.append(g8b[-2:])
                r8b = "{0:08b}".format(imgc[x][y][0])
                temp.append(r8b[-2:])
                temps =''.join(temp)
                tlist.append(temps)
        ttlist = []
        for z in tlist:
            a = z.encode("utf-8")
            ttlist.append(chr(int(a,2)))
        tt = ''.join(ttlist)
        if tt == string:
            return True
        else:
            return False

    def clean(self):
        imgc = np.copy(self.img)
        imgc[:][:][0] &= np.random.randint(253,255)
        imgc[:][:][1] &= np.random.randint(253,255)
        imgc[:][:][2] &= np.random.randint(253,255)
        imgc[:][:][3] &= np.random.randint(253,255)
        return imgc

    def embedPayload(self, payload, override=False):
        if not isinstance(payload, Payload):
            raise TypeError("invalid payload input")
        if override is False:
            if self.payloadExists():
                raise Exception("Cannot override existing payload") #this never gets triggered need to figure out why but fuck it
        if len(payload.json) > self.img.size:
            raise ValueError("Payload is too large for Carrier to hold")
        imgc = np.copy(self.img)
        ts = imgc[:,:,0].size
        r = imgc[:,:,0].reshape(ts)
        g = imgc[:,:,1].reshape(ts)
        b = imgc[:,:,2].reshape(ts)
        a = imgc[:,:,3].reshape(ts)
        js = np.fromstring(payload.json, dtype=np.uint8)
        tr = np.bitwise_and(js,3)
        tg1 = np.bitwise_and(js,12)
        tg2 = np.right_shift(tg1,2)
        tb1 = np.bitwise_and(js,48)
        tb2 = np.right_shift(tb1,4)
        ta1 = np.bitwise_and(js,192)
        ta2 = np.right_shift(ta1,6)

        ttr = np.bitwise_and(r[:tr.size],252)
        r[:tr.size] = np.bitwise_or(ttr,tr)
        ttg = np.bitwise_and(g[:tg2.size],252)
        g[:tg2.size] = np.bitwise_or(ttg,tg2)
        ttb = np.bitwise_and(b[:tb2.size],252)
        b[:tb2.size] = np.bitwise_or(ttb,tb2)
        tta = np.bitwise_and(a[:ta2.size],252)
        a[:ta2.size] = np.bitwise_or(tta,ta2)
        return imgc

    def extractPayload(self):
        imgc = np.copy(self.img)
        ts = imgc[:,:,0].size
        r = imgc[:,:,0].reshape(ts)
        g = imgc[:,:,1].reshape(ts)
        b = imgc[:,:,2].reshape(ts)
        a = imgc[:,:,3].reshape(ts)
        tr = np.bitwise_and(r,3)
        tg = np.bitwise_and(g,3)
        tb = np.bitwise_and(b,3)
        ta = np.bitwise_and(a,3)
        trbga1 = np.bitwise_or(np.left_shift(ta,6),np.left_shift(tb,4))
        trbga2 = np.bitwise_or(trbga1,np.left_shift(tg,2))
        trbga3 = np.bitwise_or(trbga2,tr)
        for i in range(len(trbga3)):
            if chr(trbga3[i]) == "}":
                break
        rcnt = trbga3[:i+1]
        js = ""
        for x in rcnt:
            js += chr(x)
        return Payload(json=js)

if __name__ == "__main__":
    def readFile(path):
        with open(path, "r") as xFile:
            content = xFile.read()
        return content
    ### test for converting rawData to json
    rD = imread(join("test_images","/home/ecegridfs/a/ee364c12/Lab11/data/dummy.png"))
    #print(rD)
    #print(rD.dtype)
    #print("__________---------")
    #text = readFile(join("test_images","/home/ecegridfs/a/ee364c12/Lab11/data/payload3.txt"))
    #rD = np.fromstring(text, dtype=np.uint8)
    #print(type(rD))
    #p1 = Payload(rawData=rD)
    #print(p1.json)

    #with self.subTest(key="Color Image"):
    #json = readFile(join(self.folder, "payload1.json"))
        #rawData = imread(join(self.folder, "payload1.png"))
        #payload = Payload(json=json)

    ### test for converting json to rawData
    #rD = None
    #cL = -1
    #js = readFile(join("test_images", "/home/ecegridfs/a/ee364c12/Lab11/data/payload1.json"))
    #p2 = Payload(json = js)
    #print(p2.rawData)
    #print(len(list(p2.rawData.shape)))
    p1 = Payload(rawData=rD)
    i1 = imread(join("test_images","/home/ecegridfs/a/ee364c12/Lab11/data/dummyCarrier.png"))
    #i1 = imread(join("test_images","/home/ecegridfs/a/ee364c12/Lab11/data/embedded3_5.png"))
    c1 = Carrier(i1)
    #c1.payloadExists()
    #c1.embedPayload(p1)
    #c1.payloadExists()
    c1.embedPayload(p1)

    #print(c1.img)
