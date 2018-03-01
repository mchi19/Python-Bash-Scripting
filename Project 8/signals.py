#! /bin/usr/env python3.4
import moduleTasks

def loadMultiple(signalNames, folderName, maxCount):
    res = {}
    for x in signalNames:
        try:
            sl, nfc = moduleTasks.loadDataFrom(x, folderName)
            #print(x, nfc)
            if nfc > maxCount:
                res[x] = []
            else: #else if nfc is less than or equal to maxCount: nfc <= MaxC
                res[x] = sl
        except:
            res[x] = None
    return res

def saveData(signalsDictionary, targetFolder, bounds, threshold):
    for key in signalsDictionary:
        fpath = targetFolder + "/" + key + ".txt"
        try:
            if moduleTasks.isBounded(signalsDictionary[key], bounds, threshold):
                with open(fpath, "w") as tfile:
                    for x in range(len(signalsDictionary[key])):
                        tfile.write("{0:.3f}".format(signalsDictionary[key][x]))
                        if not x == (len(signalsDictionary[key]) - 1): #not the last signal
                            tfile.write("\n")
        except:
            pass

if __name__ == "__main__":
    ### Part 1 ##################
    sdic = signalNames = ["AFW-481", "CIG-308", "FPT-701", "asdf"]
    folderName = "Signals"
    maxCount = 7

    sdic = loadMultiple(signalNames, folderName, maxCount)
    print(sdic["AFW-481"])

    ### Part 2 #################
    bounds = (-15.1, 16.0)
    threshold = 5
    targetFolder = "NewSignals"
    #saveData(sdic, targetFolder, bounds, threshold)