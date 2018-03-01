#! /usr/bin/env python3.4
import sys
import os

def aload():
    with open("Availability.txt", "r") as tf:
        data = tf.readlines()
        return data

def getFreeByName(names):
    rdic = {}
    dates = aload()[1].split()
    dates = dates[2:]
    ava = aload()[3:]
    for a in names:
        for name in ava:
            temp = name.split("|")
            n = temp[0].strip()
            if a == n:
                tt = []
                for x in range(1,len(temp)):
                    t = temp[x].strip()
                    if t == '1':
                        tt.append(dates[x-1])
                rdic[n] = tt
    return rdic

def getFreeByRange(date1, date2):
    if date1 > date2:
        return None
    tdic = {}
    dates = aload()[1].split()
    dates = dates[2:]
    ava = aload()[3:]
    for name in ava:
        temp = name.split("|")
        n = temp[0].strip()
        tt = []
        for x in range(1,len(temp)):
            t = temp[x].strip()
            if t == '1':
                tt.append(dates[x-1])
            tdic[n] = tt
    #print(tdic)
    ddiff = int(date2[3:]) - int(date1[3:])+1
    #print(ddiff)
    res = []
    for person in tdic:
        #print(person)
        for x in range(len(dates)):
            if dates[x] == date1:
                #print("match start date")
                count = 1
                for y in range(1,ddiff):
                    #count = 0
                    if dates[x+y] in tdic[person]:
                        count = count + 1
                    else:
                        count = 0
                    if count == ddiff :
                        #print(len(tdic[person]))
                        #if lend(tdic[person])
                        res.append(person)

            #if date1 == dates[x]:



    print(dates)
    #for person in tdic:
    #    if date1 in tdic[person] and date2 in tdic[person]:


    sres = set(res)
    return sres


def getStateByCounty(county):
    res = []
    sres = set(res)
    if not county:
        return sres
    with open("Counties.txt", "r") as tf:
        date = tf.readlines()[2:]
        #for a in data:
        #    data

    return 0

def getCountByState(state):
    if not state:
        return None


if __name__ == "__main__":

    #names = {"Sang, Chanell", "Chock, Velvet"}
    #print(getFreeByName(names))
    ##print(dic["Sang, Chanell"])

    date1 = "08/01"
    date2 = "08/05"

    print(getFreeByRange(date1, date2))

    #print(getStateByCounty("Warren"))