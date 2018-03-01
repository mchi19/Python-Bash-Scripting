#! /usr/bin/env python3.4
import sys
import os

def loadfile1():
    with open("university.txt", "r") as tfile:
        line = tfile.readlines()
        return line

def loadfile2():
    with open("courses.txt", "r") as tfile:
        line = tfile.readlines()
        return line[2:]

def getStudentInfo():
    res = {}
    fres = {}
    file = loadfile1()
    for x in range(len(file)):
        if x == 1:
            file[x] = file[x].split()
            cl = file[x][1:]
        elif x >= 3:
            temp = []
            file[x] = file[x].split("|")
            name = file[x][0].strip()
            for y in range(len(file[x])):
                if "-" not in file[x][y]:
                    tlist = (cl[y], file[x][y].strip())
                    temp.append(tlist)
                res[name] = temp[1:]
            for x in res[name]:
                fres[name] = (x[0], float(x[1]))
    return fres

def getStudentInfo2():
    res = {}
    fres = {}
    file = loadfile1()
    for x in range(len(file)):
        if x == 1:
            file[x] = file[x].split()
            cl = file[x][1:]
        elif x >= 3:
            temp = []
            file[x] = file[x].split("|")
            name = file[x][0].strip()
            for y in range(len(file[x])):
                if "-" not in file[x][y]:
                    tlist = (cl[y], file[x][y].strip())
                    temp.append(tlist)
                res[name] = temp[1:]
            for x in res[name]:
                fres[name] = (x[0], float(x[1]))
    return res


def getClassInfo():
    res = {}
    tdic = getStudentInfo2()
    for name in tdic:
        for x in tdic[name]:
            if x[0] not in res:
                res[x[0]] = []
                res[x[0]].append((name,float(x[1])))
            else:
                res[x[0]].append((name,float(x[1])))
    return res


def getBestInCourse(course):
    tdic = getClassInfo()
    res = ("name", "0")
    for x in tdic[course]:
        if float(x[1]) > float(res[1]):
            res = x
    #print(res)
    return res


def getCourseAverage(course):
    tdic = getClassInfo()
    sum = 0
    clen = len(tdic[course])
    for x in tdic[course]:
        sum = sum + float(x[1])
    res = round(sum/clen,2)
    return res


def getStudentGPA(name):
    tdic = getStudentInfo()
    tcl = loadfile2()
    tch = {}
    for x in tcl:
        x = x.split()
        tch[x[0]] = x[1]
    totc = 0
    sum = 0
    for c in tdic[name]:
        totc = totc + int(tch[c[0]])
        sum = sum + (float(c[1]) * int(tch[c[0]]))
    res = round((sum/totc),2)
    return res

if __name__ == "__main__":
    ### part 1
    #x = getStudentInfo()
    #print(x["Sadie Farkas"])

    ### part 2
    #res = getClassInfo()
    #print(len(res["ECE209"]))

    ### part 3
    res = getBestInCourse("ECE388")
    print(res)

    ### part 4 FIX THIS SHIT!!!!1 figure out how to do decimal to 2 places
    #res = getCourseAverage("ECE475")
    #print(type(res))

    ### part 4 FIX THIS SHIT!!!! figure out how to do decimal to 2 places
    #res = getStudentGPA("Floria Uribe")
    #print(type(res))

