#! /bin/usr/env python3.4

import simpleVector

def loadVectors(fileName):
    res = []
    with open(fileName, "r") as tfile:
        data = tfile.readlines()
    for line in data:
        try:
            v = simpleVector.Vector(line)
            res.append(v)
        except:
            res.append(None)
    return res

if __name__ == "__main__":
    fileName = "values.txt"
    print(loadVectors(fileName))