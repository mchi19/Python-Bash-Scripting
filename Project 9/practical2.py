#! /bin/usr/env python3.4
import sys
import re

def parseSimple(fileName):
    res = {}
    with open(fileName, "r") as tfile:
        lines = tfile.readlines()
    expr = r"\s*\"(?P<a>[\w]+)\"\s*:\s*\"(?P<b>[\d\w\s|,|\.|#|-]+)\""
    for line in lines:
        matches = re.match(expr,line)
        if matches is not None:
            key = matches.group("a")
            val = matches.group("b")
            res[key] = val
    return res

def parseLine(fileName):
    res = {}
    with open(fileName, "r") as tfile:
        lines = tfile.readlines()
    expr = r"\s*\"(?P<a>[\w]+)\"\s*:\s*\"(?P<b>[\d\w\s|,|\.|#|-]+)\""
    for line in lines:
        tm = re.findall(expr,line)
        for k,v in tm:
            res[k] = v
    return res

def parseComplex(fileName):
    res = {}
    with open(fileName, "r") as tfile:
        lines = tfile.readlines()
    expr = r"\s*\"(?P<a>[\w]+)\"\s*:\s*(?P<b>\"[\d\w\s|,|\.|#|-]+\"|[\w]+|[\d|\.]+)\,"
    for line in lines:
        matches = re.match(expr, line)
        if matches is not None:
            k = matches.group("a")
            v = matches.group("b")
            #print(k)
            #print(v)
            if v[0] == '"':
                v = v[1:-1]
                res[k] = v
            #else:
            #    if bool(v) == True:
            #        res[k] = True
            #    if bool(v) == False:
            #        print(False)
            #        res[k] = False
            #    else:
            res[k] = v
    return res


def parseComposite(fileName):
    res = {}
    with open(fileName, "r") as tfile:
        lines = tfile.readlines()
    expr = r"\s*\"(?P<a>[\w]+)\"\s*:\s*(?P<b>\"[\d\w\s|,|\.|#|-]+\"|[\w]+|[\d|\.]+)\,"
    for line in lines:
        matches = re.match(expr, line)
        if matches is not None:
            k = matches.group("a")
            v = matches.group("b")
            res[k] = v
    return res





if __name__ == "__main__":
    fn1 = "simple.json"
    fn2 = "simple2.json"
    ###part 1
    #print(parseSimple(fn1))
    ### part 2
    #print(parseLine(fn2))
    ### part3
    fn3 = "complex.json"
    #print(parseComplex(fn3))
    ### part4
    print(parseComposite(fn3))