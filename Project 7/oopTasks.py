#! /bin/usr/env python3.4

import sys
import math
from enum import Enum
from random import sample
import random
import operator

class Level(Enum):
    freshman = 1
    sophomore = 2
    junior = 3
    senior = 4

class Student(object):
    def __init__(self, id, fn, ln, lvl):
        if not type(lvl) == Level:
            raise TypeError("The argument must be an instance of the 'Level' Enum.")
        self.ID = id
        self.firstName = fn
        self.lastName = ln
        self.level = lvl

    def __str__(self):
        res = "{0}, {1} {2}, {3}".format(self.ID, self.firstName.capitalize(), self.lastName.capitalize(), self.level.name.capitalize()) #alternatively, use str.title() instead of str.capitlize()
        return res

class Circuit(object):
    def __init__(self, id, res, cap, ind, trans):
        for r in res:
            if type(r) == str:
                if not r[0] == "R":
                    raise ValueError("{0} in the resistors' list is an invalid component.".format(r))
            else:
                raise TypeError("The resistors' list has a value that isn't a string")
        for c in cap:
            if type(c) == str:
                if not c[0] == "C":
                    raise ValueError("{0} in the capacitors' list is an invalid components.".format(c))
            else:
                raise TypeError("The capacitors' list has a value that isn't a string.")
        for i in ind:
            if type(i) == str:
                if not i[0] == "L":
                    raise ValueError("{0} in the inductors' list is an invalid components.".format(i))
            else:
                raise TypeError("The inductors' list has a value that isn't a string.")
        for t in trans:
            if type(t) == str:
                if not t[0] == "T":
                    raise ValueError("{0} in the transistors' list is an invalid components.".format(t))
            else:
                raise TypeError("The transistors' list has a value that isn't a string.")
        self.ID = id
        self.resistors = res
        self.capacitors = cap
        self.inductors = ind
        self.transistors = trans

        self.resistors.sort()
        self.capacitors.sort()
        self.inductors.sort()
        self.transistors.sort()

    def __str__(self):
        res = "{0}: (R = {1:0>2d}, C = {2:0>2d}, L = {3:0>2d}, T = {4:0>2d})".format(self.ID, len(self.resistors),len(self.capacitors), len(self.inductors), len(self.transistors))
        return res

    def getDetails(self):
        res = self.ID + ":"
        for r in self.resistors:
            res = res + " {0},".format(r)
        for c in self.capacitors:
            res = res + " {0},".format(c)
        for i in self.inductors:
            res = res + " {0},".format(i)
        for t in self.transistors:
            res = res + " {0},".format(t)
        res = res[:-1]
        return res

    def __contains__(self, item):
        if not type(item) == str:
            raise TypeError("{0} is not of type 'String'.".format(item))
        cValid = ["R", "C", "L", "T"]
        if item[0] not in cValid:
            raise ValueError("{0} is not a known component".format(item))

        if item in self.resistors:
            return True
        if item in self.capacitors:
            return True
        if item in self.inductors:
            return True
        if item in self.transistors:
            return True
        return False

    def __add__(self, other):
        if type(other) == Circuit:
            odl = ['0','1','2','3','4','5','6','7','8','9']
            temp = random.sample(odl,5)
            id = ''.join(temp)
            tr = self.resistors
            tc = self.capacitors
            ti = self.inductors
            tt = self.transistors
            for x in other.resistors:
                if x not in self.resistors:
                    tr.append(x)
            for y in other.capacitors:
                if y not in self.capacitors:
                    tc.append(y)
            for z in other.inductors:
                if z not in self.inductors:
                    ti.append(z)
            for w in other.transistors:
                if w not in self.transistors:
                    tt.append(w)
            return Circuit(id, tr, tc, ti, tt)
        if (not type(other) == Circuit) and (not type(other) == str):
            raise TypeError("Argument is an invalid type.")

        if self.__contains__(other) == True:
            return self
        if other[0] == "R":
            self.resistors.append(other)
            self.resistors.sort()
        if other[0] == "C":
            self.capacitors.append(other)
            self.capacitors.sort()
        if other[0] == "L":
            self.inductors.append(other)
            self.inductors.sort()
        if other[0] == "T":
            self.transistors.append(other)
            self.transistors.sort()
        return self

    ### allows "+" operator to be commutative
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if self.__contains__(other) == False:
            return self
        if other in self.resistors:
            self.resistors.remove(other)
            #remove other from the list
        if other in self.capacitors:
            self.capacitors.remove(other)
        if other in self.inductors:
            self.inductors.remove(other)
        if other in self.transistors:
            self.transistors.remove(other)
        return self

class Project(object):
    def __init__(self, id, part, circ):
        if not part:
            raise ValueError("Argument is an empty list.")
        if not type(part) == list:
            raise ValueError("The Participants' list is not a valid list.")
        if type(part) == list:
            for x in part:
                if not type(x) == Student:
                    raise ValueError("Not all elements in the Participants' list are of class 'Student'.")

        if not circ:
            raise ValueError("Arguement is an empty list.")
        if not type(circ) == list:
            raise ValueError("The Circuits' list is not a valid list.")
        if type(circ) == list:
            for y in circ:
                if not type(y) == Circuit:
                    raise ValueError("Not all elements in the Circuits' list are of class 'Circuit'.")
        self.ID = id
        self.participants = part
        self.circuits = circ

        self.participants.sort(key=operator.attrgetter('ID'))
        self.circuits.sort(key=operator.attrgetter('ID'))

    def __str__(self):
        res = "{0}: {1:0>2d} Circuits, {2:0>2d} Participants".format(self.ID, len(self.circuits), len(self.participants))
        return res

    def getDetails(self):
        res = "{0}\n\nParticipants:".format(self.ID)
        for x in self.participants:
            res = res + "\n{0}".format(x)
        res = res + "\n\nCircuits:"
        for y in self.circuits:
            res = res + "\n{0}".format(y.getDetails())
        return res

    def __contains__(self, item):
        if type(item) == str:
            for x in self.circuits:
                if x.__contains__(item) == True:
                    return True
            return False

        elif type(item) == Circuit:
            for x in self.circuits:
                if x.ID == item.ID:
                    return True
            return False

        elif type(item) == Student:
            for x in self.participants:
                if x.ID == item.ID:
                    return True
            return False
        else:
            raise TypeError("Argument is not a valid type.")

    def __add__(self, other):
        if type(other) == Circuit:
            for x in self.circuits:
                if x.ID == other.ID:
                    return self
            self.circuits.append(other)
            self.circuits.sort(key=operator.attrgetter('ID'))
            return self
        elif type(other) == Student:
            for x in self.participants:
                if x.ID == other.ID:
                    return self
            self.participants.append(other)
            self.participants.sort(key=operator.attrgetter('ID'))
            return self
        else:
            raise TypeError("Argument is not a valid type.")

    def __sub__(self, other):
        if type(other) == Circuit:
            for x in self.circuits:
                if x.ID == other.ID:
                    self.circuits.remove(x)
            return self
        elif type(other) == Student:
            for x in self.participants:
                if x.ID == other.ID:
                    self.participants.remove(x)
            return self
        else:
            raise TypeError("Argument is not a valid type.")

class Capstone(Project):
    def __init__(self, id, part, circ):
        Project.__init__(self, id, part, circ)
        for x in self.participants:
            if not x.level == Level.senior:
                raise ValueError("Student is not a Senior.")

    def __add__(self, other):
        if type(other) == Student:
            if other.level == Level.senior:
                Project.__add__(self, other)
                return self
            else:
                raise TypeError("Student is not a Senior.")
        else:
            raise TypeError("Argument is not a student.")

if __name__ == "__main__":

    ###STUDENT CLASS
    s1 = Student("15487-79431", "john", "smith", Level.senior)
    s2 = Student("11111-11111", "Myra", "Fu", Level.senior)
    s3 = Student("22222-22222", "Michael", "Williams", Level.senior)
    s4 = Student("22111-11122", "Michelle", "Williams", Level.senior)
    #s5 = Student("111", "hi", "there", 'senior')
    #print(s1)

    ###CIRCUIT CLASS
    c1 = Circuit("99887", ["R206.298", "R436.943"], ["C1.1", "C1.5", "C2.3", "C1.3", "C1.8", "C5.6", "C4.42", "C2.62", "C3.79", "C9.8", "C10.2"], ["L1.1"], [])#, ["T1.1", "T1.2", "T1.5"])
    c2 = Circuit("11023", ["R1.1", "R1.5", "R2.3", "R1.3"], ["C4.8", "C4.6", "C2.42", "C5.62", "C1.79", "C10.8", "C10.1"],["L1.1", "L12.5", "L66.2"], ["T1.24", "T90.1"])
    c3 = Circuit("10101", ["R5.7"], ["C6.23"], ["L11.51"], ["T8.2"])
    f = [1, 2, 3]
    #print(c1)
    #print(c1.getDetails())
    a = "L1.1"
    #print(a in c3)
    c1 = c1 + "C1.1"
    #print(c1)
    #print(c1.getDetails())
    e = c1 + c1
    #print(e)
    #print(e.getDetails())
    #e = c1 - "C111.1"
    #print(e)
    #print(e.getDetails())

    ###PROJECT CLASS
    p1 = Project("38753067-e3a8-4c9e-bbde-cd13165fa21e", [s1, s2, s3], [c1, c2])
    p2 = Project("31111111-e333-4111-bbde-c111111e111e", [s4], [c3])
    print(p1)
    print(p1.getDetails())
    #a = "1111.1"
    #print(s3 in p1)
    #print(p1.getDetails())
    g = p1 + s1
    print(g)
    print(g.getDetails())

    ###CAPSTONE CLASS
    cap1 = Capstone("1111", [s1, s2, s3], [c1, c2])
    #print(cap1)
    #print(cap1.getDetails())
    cap2 = cap1 + s2
    #print(cap2)
    #print(cap2.getDetails())
    #cap3 = cap2 - s2
    #print(cap3)
    #print(cap3.getDetails())

