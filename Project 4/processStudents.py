#! /usr/bin/env python3.4
import sys
import os

def getRegistration():
    sdic = {}
    for file in os.listdir("Classes"):
        with open ("./Classes/"+file, "r") as tf:
            data = tf.readlines()
            temp = []
            for x in data:
                temp.append(x.strip())
            #print(temp)
            for name in temp:
                sdic[name] = []
    for file in os.listdir("Classes"):
        with open ("./Classes/"+file, "r") as ttf:
            td = ttf.readlines()
            for x in td:
                a = x.strip()
                if a in sdic:
                    sdic[a].append(file[0:6])
    #print(sdic['Saran Loveall'])
    #print(sdic['Selma Zinck'])
    #print(sdic['Portia Reiter'])
    #print(sdic['Raymundo Loan'])
    return sdic

def getCommonClasses(studentName1, studentName2):
    res = []
    sdic = getRegistration()
    if (studentName1 not in sdic) or (studentName2 not in sdic):
        return None
    for x in sdic[studentName1]:
        if x in sdic[studentName2]:
            res.append(x)
    sres = set(res)
    return sres

#main block
if __name__ == "__main__":

    ### 1
    #print(getRegistration())

    ### 2
    studentName1 = 'Tamatha Granderson'
    studentName2 = 'Tasha Shell'
    print(getCommonClasses(studentName1, studentName2))