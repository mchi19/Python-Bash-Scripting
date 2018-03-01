#! /bin/usr/env python3.4
import sys
import re

def parseXML(xmlNode):
    m = re.findall(r"([a-z]+)=\"(.*?)\"", xmlNode)
    m.sort()
    return m

def captureNumbers(sentence):
    expr = r"[\+|\-]?\d+\.\d+[e|E][\+|\-][\d]+|[\+|\-]?\d+\.\d+|[\+|\-]?\d+"
    m = re.findall(expr, sentence,re.I)
    return m








if __name__ == "__main__":

    ### 1
    #xmlNode = '<person  name="Irene Adler" gender="female"  age="35" />'
    #print(parseXML(xmlNode))


    ### 2
    sentence = "With the electron's charge being -1.6022e-19, some choices you have are -110, -32.0, and +55. Assume that pi equals 3.1415, 'e' equals 2.7 and Na is +6.0221E+023."
    print(captureNumbers(sentence))