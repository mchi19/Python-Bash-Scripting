#! /bin/usr/env python3.4

from localBank import *

def loadBankData(dataFileName):
    rb = Bank()
    with open(dataFileName, "r") as tfile:
        data = tfile.readlines()
        tdata = data[3:]
    #print(tdata)
    for x in tdata:
        #print(x)
        temp = x.split("|")
        #print(temp[0])
        temp[0] = temp[0].strip()
        #print(temp[0])
        #print(temp[1])

        temp[1] = temp[1].strip()
        temp[2] = temp[2].strip()
        #print(temp)
        if temp[1] not in rb.accounts:
            #if temp[2][0] == '('
            #    rb[temp[1]] = temp[2][1:-1]
            #else:
            rb.accounts[temp[1]] = temp[2]
        else:
            if temp[2][0] == '(':
                #rb[temp[1]] = temp[2][1:-1]
                print(float(temp[2][2:-1]))
                trans = Transaction('W', float(temp[2][2:-1]))
                rb.applyTransaction(temp[1], trans)
            else:
                trans = Transaction('D', float(temp[2][1:]))
                rb.applyTransaction(temp[1], trans)
    return rb

def getTotalBalanceByPerson(bank, person):
    pass

def getBalances(bank):
    pass


if __name__ == "__main__":
    print(loadBankData("transactions.txt"))