#! /usr/bin/env python3.4
import sys

def loadfile():
    with open("sequence.txt", "r") as tfile:
        xyz = tfile.read()
    return xyz

def find(pattern):
    data = loadfile()
    res = []
    temp = []
    counter = 0
    i = 0
    j = 0
    dlen = len(data)
    plen = len(pattern)
    while j < dlen:
        if (pattern[i] == data[j]) or (pattern[i] == 'X'):
            temp.append(data[j])
            i += 1
            counter += 1
        else:
            i = 0
            temp = []
            j = j - counter
            counter = 0
        if counter == plen:
            match="".join(temp)
            res.append(match)
            temp = []
            i = 0
        j += 1
    return res

def getStreakProduct(sequence, maxSize, product):
    slen = len(sequence)
    res = []
    temp = []
    i = 0
    while i < slen:
        temp.append(sequence[i])
        tlen = len(temp)
        j = 0
        if (tlen == maxSize):
            tprod = 1
            tarr = []
            while j < tlen:
                tprod = tprod * int(temp[j])
                tarr.append(temp[j])
                if j >= 1:
                    if tprod == product:
                        match = "".join(tarr)
                        res.append(match)
                j += 1
            if i == (slen - 1):
                k = 0
                ltarr = temp[k+1:]
                ltlen = len(ltarr)
                while len(ltarr) > 1:
                    tprod = 1
                    tarr = []
                    while k < len(ltarr):
                        tprod = tprod * int(ltarr[k])
                        tarr.append(ltarr[k])
                        if k >= 1:
                            if tprod == product:
                                match = "".join(tarr)
                                res.append(match)
                        k += 1
                    k = k - len(ltarr)
                    ltarr = ltarr[k+1:]
            temp = []
            i = i - maxSize + 1
        i += 1
    return res

def writePyramids(filePath, baseSize, count, char):
    with open(filePath, "w") as tfile:
        height = int((baseSize + 1 ) / 2)
        whites=baseSize
        blox = 1
        iws = int(baseSize/2)
        ews = int(baseSize/2)
        for h in range(0, height):
            for x in range(0, iws):
                tfile.write(" ")
                y = 0
            #while y < count:
            for y in range(0, count): #number of pyramids to print
                for z in range(0, blox): #number of chars to print per line of pyramid
                   tfile.write("{0}".format(char))
                if y == (count - 1):
                    for w in range(0, ews):
                        tfile.write(" ")
                else:
                    for l in range(0, whites): #number of whitespaces to print per line of pyramid
                        tfile.write(" ")
                #y += 1
            iws -= 1
            ews -= 1
            whites -= 2
            blox += 2
            tfile.write("\n")
    return 0

def getStreaks(sequence, letters):
    res = []
    llen = len(letters)
    slen = len(sequence)
    x = 0
    flag = 1
    temp = []
    while x < slen:
        if sequence[x] in letters:
            if flag == 1:
                prev = sequence[x]
                temp.append(sequence[x])
                flag = 0
            else:
                if sequence[x] == prev:
                    temp.append(sequence[x])
                else:
                    streak = "".join(temp)
                    res.append(streak)
                    temp = []
                    temp.append(sequence[x])
                    prev = sequence[x]
        else:
            prev = sequence[x]
        x += 1
    if not temp:
        return res
    streak = "".join(temp)
    res.append(streak)
    return res

def findNames(nameList, part, name):
    res = []
    tname = name.lower()
    nl_len = len(nameList)
    for person in nameList:
        x = person.split()
        if "F" in part:
            if x[0].lower() == tname:
                res.append(person)
        if "L" in part:
            if x[1].lower() == tname:
                res.append(person)
    return res

def convertToBoolean(num, size):
    res = []
    bn = "{0:b}".format(num)
    bnlen= len(bn)
    x = 0
    if size > bnlen:
        for y in range(size-bnlen):
            res.append(bool(0))
    while x < bnlen:
        if bn[x] == '1':
            res.append(bool(1))
        else: #if bn[x] == '0':
            res.append(bool(0))

        x += 1
    return res

def convertToInteger(boolList):
    if type(boolList) is not list:
        return None
    for x in boolList:
        if type(x) is not bool:
            return None
    if not boolList:
        return None
    temp = []
    for y in boolList:
        if y == True:
            temp.append("1")
        if y == False:
            temp.append("0")
    num = "".join(temp)
    res = int(num,2)
    return res



#main block
if __name__ == "__main__":

    ######1
    pattern="X38XX2"
    #find(pattern)
    print(find(pattern))

    ######2
    #sequence = "54789654321687984"
    #sequence = "14822"
    #maxSize = 3
    #product = 100
    #print(getStreakProduct(sequence, maxSize, product))

    ######3
    #writePyramids('pyramid15a.txt', 15, 5, '*')

    #####4
    #sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"
    #letters = "SAQT"
    #print(getStreaks(sequence, letters))

    #####5
    #nameList = ["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"]
    #part = "FL"
    #name = "Johnson"
    #print(findNames(nameList, part, name))

    ######6
    #print(convertToBoolean(135, 12))
    #print(convertToBoolean(9, 3))

    #####7
    #bList = [True, False, False, False, False, True, True, True]
    #bList = []
    #print(convertToInteger(bList))
    #bList = [False, True, False]
    #print(convertToInteger(bList))
