#! /usr/bin/env python3.4
import sys

def getTotal(accounts):
    x = 0
    alen = len(accounts)
    res = []
    while x < alen:
        sum = 0
        temp = accounts[x].split('$')
        for y in range(1, len(temp)):
            tv = temp[y].strip()
            sum += float(tv)
        tsum = round(sum,2)
        res.append(tsum)
        x += 1
    return res

def getDoublePalindromes():
    res = []
    for x in range(10, 1000000):
        temp = "{0}".format(x)
        nlst = list(temp)   #reversed list
        alst = list(temp)   #normal list
        tl = len(nlst)
        nlst.reverse()
        if nlst == alst:
            bna ="{0:b}".format(x) #normal list
            bnb ="{0:b}".format(x) #reversed list
            lbna = list(bna)
            lbnb = list(bnb)
            lbnb.reverse()
            if lbnb == lbna:
                res.append(x)
    return res



#main block
if __name__ == "__main__":

    accounts = ["John Smith:   $3.25   $15.98   $56.90   $100.45   $37.66   $81.72   $0.34  ", "George Teal: $1.00 $2.00 $3.00   $4.01  ", "Christine Doyle:   $10.51    $22.49    $12.00 $5.33 $100.00  "]

    print(getTotal(accounts))

    #print(getDoublePalindromes())
    print(len(getDoublePalindromes()))
