#! /usr/bin/env python3.4
import sys
import os

def loadpfile():
    with open("projects.txt", "r") as tfile:
        line = tfile.readlines()[2:]
        return line

def loadsfile():
    with open("students.txt", "r") as tfile:
        line = tfile.readlines()[2:]
        return line

def getComponentCountByProject(projectID):
    file = loadpfile()
    tlen = len(file)
    tf = []
    flag = 0 #indicates if valid projectID
    for i in range(tlen):
        a = file[i].split()
        if a[1] == projectID:
            tr = ()
            with open("Circuits/circuit_{0}.txt".format(a[0]), "r") as temp:
                data = temp.readlines()
                tdata = data[4].split(',')
                for x in tdata:
                    x.strip() ######check this maybe
                    if x not in tf:
                        tf.append(x)
            flag = 1
    if flag == 0:
        return None
    cap=0
    rstr=0
    ind=0
    trans=0
    for z in tf:
        if 'C' in z:
            cap += 1
        elif 'R' in z:
            rstr += 1
        elif 'T' in z:
            trans += 1
        elif 'L' in z:
            ind += 1
    res = (rstr, ind, cap, trans)
    return res

def getComponentCountByStudent(studentName):
    cap=0
    rstr=0
    ind=0
    trans=0
    res = ()
    file = loadsfile()
    tlen = len(file)
    temp = []
    ttf = []
    for i in range(tlen):
        a,b = file[i].split('|')
        ta = a.strip()
        tb = b.strip()
        temp.append(ta)
        temp.append(tb)

    if studentName not in temp:
        return None

    llen = len(temp)
    for x in range(llen):
        if temp[x] == studentName:
            sid = temp[x+1]

    for filename in os.listdir("./Circuits"):
        with open("./Circuits/"+filename, "r") as tf:
            data = tf.readlines()
            tidl = data[1].split(',')
            for y in tidl:
                tp = y.strip()
                if sid == tp:
                    print(filename)
                    tdata = data[4].split(',')
                    for x in tdata:
                        x.strip()
                        if x not in ttf:
                            ttf.append(x)
    for z in ttf:
        if 'C' in z:
            cap += 1
        elif 'R' in z:
            rstr += 1
        elif 'T' in z:
            trans += 1
        elif 'L' in z:
            ind += 1
    res = (rstr, ind, cap, trans)
    return res

def getParticipationByStudent(studentName):
    tdata = loadsfile()
    tlen = len(tdata)
    temp = []
    rset = {}
    ###get the students ID from studentname
    for i in range(tlen):
        a,b = tdata[i].split('|')
        ta = a.strip()
        tb = b.strip()
        temp.append(ta)
        temp.append(tb)
    sid = ""
    ttlen = len(temp)
    for j in range(ttlen):
        if (temp[j] == studentName):
            sid = temp[j+1]
    print(sid)
    if not sid:
        return None
    ttf = []
    ###checking each circuit file in circuits folder
    for filename in os.listdir("Circuits"):
        with open("./Circuits/"+filename, "r") as tf:
            data = tf.readlines()
            tidl = data[1].split(',')
            for y in tidl:
                tp = y.strip()
                if sid == tp:
                    print(filename)
                    mfn = filename #matching filename
                    tp = loadpfile()
                    for line in tp:
                        c = line.split()
                        if c[0] in mfn:   #c[0] is a substring of circuit then append the projectID
                            ttf.append(c[1])
    sttf = set(ttf)
    print(len(sttf))
    return sttf

def getParticipationByProject(projectID):
    temp = []
    file = loadpfile()
    cnl = []
    for line in file:
        a = line.split()
        if a[1] == projectID:
            cnl.append(a[0]) #circuit number
    if not cnl:
        return None
    tpl = []
    for cn in cnl:
        with open("./Circuits/circuit_"+cn+".txt", "r") as tf:
            data = tf.readlines()
            pl = data[1].split(',')
            for person in pl:
                b = person.strip()
                if b not in tpl:
                    tpl.append(b)
    sdata = loadsfile()
    stdic = {}

    for i in range(len(sdata)):
        a,b = sdata[i].split('|')
        ta = a.strip() #name
        tb = b.strip() #studentid
        stdic[tb] = ta
    for i in tpl:
        if i in stdic:
            temp.append(stdic[i])
    print(len(temp))
    sret = set(temp)

    return sret

def getProjectByComponent(components):
    dcomp = {}
    for comp in components:
        tt = []
        temp = []
        for file in os.listdir("Circuits"):
            with open("./Circuits/"+file, "r") as tf:
                data = tf.readlines()
            tdata = data[4].split(',')
            for c in tdata:
                c = c.strip()
                if comp == c:
                    temp.append(file[8:13])
        proj = loadpfile()
        for line in proj:
            line = line.split()
            if line[0] in temp:
                if line[0] not in tt:
                    tt.append(line[1])
        stt = set(tt)
        dcomp[comp] = stt
    return dcomp

def getStudentByComponent(components):
    dcomp = {}
    for comp in components:
        tt = []
        temp = []
        for file in os.listdir("Circuits"):
            with open("./Circuits/"+file, "r") as tf:
                data = tf.readlines()
            tdata = data[4].split(',')
            tid = data[1].split(',')
            for c in tdata:
                c = c.strip()
                if comp == c:
                    for x in tid:
                        x = x.strip()
                        temp.append(x)
        studs = loadsfile()
        ndic = {}
        for line in studs:
            a,b = line.split('|')
            ta = a.strip()
            tb = b.strip()
            ndic[tb] = ta
        for x in temp:
            if x in ndic:
                tt.append(ndic[x])
        stt = set(tt)
        dcomp[comp] = stt
    return dcomp

def getComponentByStudent(studentNames):
    sdata = loadsfile()
    ndic = {}
    rdic = {} #returning dictionary
    for x in sdata:
        a, b = x.split('|')
        ta = a.strip()
        tb = b.strip()
        ndic[ta] = tb
    for name in studentNames:
        sid = ndic[name]
        temp = []
        for file in os.listdir("Circuits"):
            with open("./Circuits/"+file, "r") as tf:
                data = tf.readlines()
                tp = data[1].split(',') #temp participant list
                if sid in tp:
                    tc = data[4].split(',')
                    for y in tc:
                        y = y.strip()
                        temp.append(y)
        stemp = set(temp)
        rdic[name] = stemp
    return rdic

def getCommonByProject(projectID1, projectID2):
    res = []
    pdata = loadpfile()
    chckpid = []
    pdic = {}

    for x in pdata:
        temp = x.split()
        chckpid.append(temp[1])
    if (projectID1 not in chckpid) or (projectID2 not in chckpid):
        return None
    t1 = []
    t2 = []
    for y in pdata:
        t = y.split()
        if t[1] == projectID1:
            t1.append(t[0])
        if t[1] == projectID2:
            t2.append(t[0])
    temp1 = []
    for filenum in t1:
        with open("./Circuits/circuit_"+filenum+".txt", "r") as tf1:
            data1 = tf1.readlines()
        tdata1 = data1[4].split(',')
        for comp in tdata1:
            a = comp.strip()
            temp1.append(a)
    temp2 = []
    for filenum in t2:
        with open("./Circuits/circuit_"+filenum+".txt", "r") as tf2:
            data2 = tf2.readlines()
        tdata2 = data2[4].split(',')
        for comp in tdata2:
            b = comp.strip()
            temp2.append(b)
    pdic[projectID1] = set(temp1)
    pdic[projectID2] = set(temp2)

    for comp in pdic[projectID1]:
        if comp in pdic[projectID2]:
            res.append(comp)

    res.sort()
    return res

def getCommonByStudent(studentName1, studentName2):
    res = []
    sdata = loadsfile()
    ndic = {}
    for x in sdata:
        a,b = x.split('|')
        ta = a.strip()
        tb = b.strip()
        ndic[ta] = tb
    if (studentName1 not in ndic) or (studentName2 not in ndic):
        return None
    t1 = []
    t2 = []
    for file in os.listdir("Circuits"):
        with open("./Circuits/"+file, "r") as tf:
            lid = []
            lcomp = []
            data = tf.readlines()
            tid = data[1].split(',')
            tcomp = data[4].split(',')
            for y in tid:
                t = y.strip()
                lid.append(t)
            for z in tcomp:
                lcomp.append(z.strip())
            if ndic[studentName1] in lid:
                for x1 in lcomp:
                    t1.append(x1)
            if ndic[studentName2] in lid:
                for x2 in lcomp:
                    t2.append(x2)
    tdic = {}
    tdic[studentName1] = set(t1)
    tdic[studentName2] = set(t2)
    for comp in tdic[studentName1]:
        if comp in tdic[studentName2]:
            res.append(comp)
    res.sort()
    return res

def getProjectByCircuit():
    p = loadpfile()
    rdic = {}
    for line in p:
        data = line.split()
        rdic[data[0]] = []
    for line in p:
        data = line.split()
        if data[1] not in rdic[data[0]]:
            rdic[data[0]].append(data[1])
    return rdic

def getCircuitByStudent():
    s = loadsfile()
    niddic = {}
    rdic = {}
    temp = []
    for x in s:
        a,b = x.split('|')
        ta = a.strip()
        tb = b.strip()
        niddic[ta] = tb
    for name in niddic:
        t = []
        for file in os.listdir("Circuits"):
            with open("./Circuits/"+file,"r") as tf:
                data = tf.readlines()
            tid = data[1].split(',')
            tcomp = data[4].split(',')
            t1 = []
            for y in tid:
                t1.append(y.strip())
            t2 = []
            for z in tcomp:
                t2.append(z.strip())
            if niddic[name] in t1:
                for comp in t2:
                    t.append(comp)
        rdic[name] = t
    return rdic

def getCircuitByStudentPartial(studentName):
    s = loadsfile()
    tdic = {}
    for line in s:
        a,b = line.split('|')
        ta = a.strip()
        tb = b.strip()
        if studentName in ta:
            temp = getCircuitByStudent()
            tdic[ta] = temp[ta]
    if not tdic:
        return None
    return tdic


#main block
if __name__ == "__main__":

    ### 1
    #projectID = '90BE0D09-1438-414A-A38B-8309A49C02EF'
    #print(getComponentCountByProject(projectID))
    #print(type(getComponentCountByProject(projectID)))

    ### 2
    #studentName = 'Adams, Keith'
    #print(getComponentCountByStudent(studentName))

    ### 3
    #studentName = 'Adams, Keith'
    #print(getParticipationByStudent(studentName))

    #### 4
    #projectID = '082D6241-40EE-432E-A635-65EA8AA374B6'
    #print(getParticipationByProject(projectID))

    ### 5
    #components = {'T475.274', 'C471.636'} #, 'L760.824', 'R497.406', 'T77.624', 'T426.533', 'C313.400', 'R591.569', 'T471.600', 'T208.114'}
    #print(getProjectByComponent(components))

    ### 6
    #components = {'T475.274', 'C471.636'}
    #print(getStudentByComponent(components))

    ### 7
    #studentNames = {'Adams, Keith', 'Alexander, Carlos'}
    #print(getComponentByStudent(studentNames))


    ### 8
    #projectID1 = '082D6241-40EE-432E-A635-65EA8AA374B6'
    #projectID2 = '90BE0D09-1438-414A-A38B-8309A49C02EF'
    #print(getCommonByProject(projectID1, projectID2))

    ### 9
    #studentName1 = 'Adams, Keith'
    #studentName2 = 'Alexander, Carlos'
    #print(getCommonByStudent(studentName1, studentName2))

    ### 10
    #print(getProjectByCircuit())

    ### 11
    #print(getCircuitByStudent())

    ### 12
    studentName = 'Adams'
    print(getCircuitByStudentPartial(studentName))