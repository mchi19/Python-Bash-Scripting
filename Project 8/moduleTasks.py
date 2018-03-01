#! /bin/usr/env python3.4
import sys
import math
import copy
import os
import re
from exModule import runNetworkCode

def checkNetwork(**kwargs):
    try:
        runNetworkCode(**kwargs)
    except ConnectionError:
        raise
    except OSError as ose:
        return "An issue encountered during runtime. The name of the error is: {0}".format(ose.__class__.__name__)
    except:
        return False
    else:
        return True

def isOK(signalName):
    expr = r"^[A-Z]{3}\-[0-9]{3}$"
    if re.search(expr, signalName):
        return True
    else:
        return False

def loadDataFrom(signalName, folderName):
    nfc = 0
    rl = []
    if not (isOK(signalName)):
        raise ValueError("{0} is invalid".format(signalName))
    fpath = folderName + "/" + signalName + ".txt"
    try:
        with open(fpath, "r") as tfile:
            data = tfile.readlines()
    except:
        raise OSError("{0}.txt cannot be found in the {1} folder.".format(signalName, folderName))
    for line in data:
        try:
            rl.append(float(line))
        except:
            nfc += 1
    res = (rl, nfc)
    return res

def isBounded(signalValues, bounds, threshold):
    if len(signalValues) == 0:
        raise ValueError("Signal contains no data.")
    ovc = 0
    lb = bounds[0]
    ub = bounds[1]
    for val in signalValues:
        if not lb < val < ub:
            ovc += 1
    #print(ovc)
    if ovc > threshold:
        return False
    return True

if __name__ == "__main__":
    ### Part 1 #################
    #print(checkNetwork(**kwargs))

    ### Part 2 #################

    ### a
    signalName = "AFW-481"
    #print(isOK(signalName))

    ### b
    folderName = "Signals"
    signalValues, nfc = loadDataFrom(signalName, folderName)
    print(signalValues, nfc)
    #print(loadDataFrom(signalName, folderName))

    ### c
    bounds = (-15.00, 20.11)
    threshold = 5
    print(isBounded(signalValues, bounds, threshold))