#! /bin/usr/env python3.4
import sys
import re
from uuid import UUID

def getUrlParts(url):
    expr= r"//(?P<ba>(\w|\-)+\.(\w|\-)+\.(\w|\-)+)/(?P<con>\w+)/(?P<act>\w+)\?"
    matches = re.search(expr, url)
    BaseAction = matches.group("ba")
    Controller = matches.group("con")
    Action = matches.group("act")
    res = (BaseAction, Controller, Action)
    return res

def getQueryParameters(url):
    res = []
    expr = r"(?P<a>(\w|\-|\.)+)=(?P<b>(\w|\-|\.)+)"
    matches = re.findall(expr, url)
    for x in matches:
        temp = []
        temp.append(x[0])
        temp.append(x[2])
        res.append(tuple(temp))
    return res

def getSpecial(sentence, letter):
    expr = r"\b({0}\w*[^{0}\W]|[^{0}\W]\w*{0})\b".format(letter)
    matches = re.findall(expr, sentence, re.I)
    return matches

def getRealMAC(sentence):
    #expr = r"(([0-9a-fA-F]{2})(-|:)){5}([0-9a-fA-F]{2})"
    expr = r"(((([a-fA-F0-9]{2})(-|:)){5})([a-fA-F0-9]{2}))"
    res = re.search(expr, sentence)
    if not res:
        return None
    else:
        return res.group(0)

def genData():
    elist = [] #employee list
    with open("Employees.txt", "r") as tf:
        data = tf.readlines()
        #expr = r"(?P<name>\w+,? \w+)([,;\s]+)(?P<ID>({?)\w{8}(\-?)((\w{4}(\-?)){3})\w{12}(}?))([,;\s]+)(?P<phone>(\(?)\d{3}(\)?)( |\-)?\d{3}(\-?)\d{4})([,;\s]+)(?P<state>)"
    name_expr = "\w+,? \w+"
    ID_expr = "({?)\w{8}(\-?)((\w{4}(\-?)){3})\w{12}(}?)"
    phone_expr = "(\(?)\d{3}(\)?)( |\-)?\d{3}(\-?)\d{4}"
    state_expr = "[\w ]+"
    space_expr = "([,;\s]+)"
    expr = r"(?P<name>{0}){4}(?P<ID>{1})?{4}(?P<phone>{2})?{4}(?P<state>{3})?".format(name_expr, ID_expr, phone_expr, state_expr, space_expr)
    for line in data:
        matches = re.match(expr, line)
        name = matches.group("name")
        ID = matches.group("ID")
        phone = matches.group("phone")
        state = matches.group("state")
        if name:
            tn = chkName(name) #calls function to fix name format
        else:
            tn = name
        if ID:
            tid = chkID(ID) #calls function to fix ID format
        else:
            tid = ID
        if phone:
            tphone = chkPhone(phone) #calls function to fix phone number format
        else:
            tphone = phone
        temp = [tn, tid, tphone, state]
        #print(temp)
        elist.append(temp)
    return elist

def chkName(name):
    expr = r"\w+"
    if ',' in name:
        m = re.findall(expr, name)
        fl = "{0} {1}".format(m[1], m[0])
    else:
        fl = name
    return fl

def chkID(ID):
    temp = "{"
    expr = r"\w"
    m = re.findall(expr,ID)
    jm = "".join(m)
    temp = "{" + jm + "}"
    pid = str(UUID(temp))
    return pid

def chkPhone(phone):
    expr = r"\d"
    m = re.findall(expr, phone)
    number = "({0}) {1}-{2}".format((''.join(m[0:3])), (''.join(m[3:6])), (''.join(m[6:])))
    return number

def getRejectedEntries():
    elist = genData()
    res = []
    for entry in elist:
        if not entry[1] and not entry[2] and not entry[3]:
            res.append(entry[0])
    res.sort()
    #print("")
    #print(len(res))
    return res

def getEmployeesWithIDs():
    rdic = {}
    elist = genData()
    for entry in elist:
        if entry[1]:
            rdic[entry[0]] = entry[1]
    #print("")
    #print(len(rdic))
    return rdic

def getEmployeesWithoutIDs():
    elist = genData()
    res = []
    for entry in elist:
        if (entry[2] or entry[3]) and not entry[1]:
            res.append(entry[0])
    #print("")
    #print(len(res))
    res.sort()
    return res

def getEmployeesWithPhones():
    rdic = {}
    elist = genData()
    for entry in elist:
        if entry[2]:
            rdic[entry[0]] = entry[2]
    #print("")
    #print(len(rdic))
    return rdic

def getEmployeesWithStates():
    rdic = {}
    elist = genData()
    for entry in elist:
        if entry[3]:
            rdic[entry[0]] = entry[3]
    #print("")
    #print(len(rdic))
    return rdic

def getCompleteEntries():
    rdic = {}
    elist = genData()
    for entry in elist:
        if entry[1] and entry[2] and entry[3]:
            rdic[entry[0]] = (entry[1], entry[2], entry[3])
    #print("")
    #print(len(rdic))
    return rdic


if __name__ == "__main__":

    ### 1
    url="http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"
    print(getUrlParts(url))

    ### 2
    url="http://www.google.com/Math/Const?Pi=3.14&Max_Int=65536&What_Else=Not-Here"
    print(getQueryParameters(url))

    ### 3
    s = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week."
    print(getSpecial(s, "t"))

    ### 4
    s = "OnTuesdays and Thur18-2C:3A:4E:F9:34Dsdays. 58:1C:0A:6E:39:4D"
    #print(type(getRealMAC(s)))
    print(getRealMAC(s))

    ### 5
    print(getRejectedEntries())

    ### 6
    print(getEmployeesWithIDs())

    ### 7
    print(getEmployeesWithoutIDs())

    ### 8
    print(getEmployeesWithPhones())

    ### 9
    print(getEmployeesWithStates())

    ### 10
    print(getCompleteEntries())