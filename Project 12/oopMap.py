import sys
import os
import math

class Entry(object):
    def __init__(self, k=0, v=""):
        if not isinstance(k,int):
            raise TypeError("k is not a valid integer input")
        if type(v) is not str:
            raise TypeError("v is not a valid string input")
        self.key = k
        self.value = v

    def __str__(self):
        res = "({0}: \"{1}\")".format(self.key, self.value)
        return res

    def __hash__(self):
        t =(self.key, self.value)
        return hash(t)

class Lookup(object):
    def __init__(self, name):
        if name is None:
            raise ValueError("Invalid input for name")
        self._name = name
        self._entrySet = set()

    def __str__(self):
        res = "[\"{0}\": {1:02d} Entries]".format(self._name, len(self._entrySet))
        return res

    def addEntry(self, entry):
        if entry in self._entrySet:
            raise ValueError("Error, entry already exists")
        else:
            self._entrySet.add(entry)

    def removeEntry(self,entry):
        if entry not in self._entrySet:
            raise KeyError("Error, entry does not exist")
        else:
            self._entrySet.remove(entry)

    def getEntry(self, key):
        flag = 0
        for ent in self._entrySet:
            if ent.key == key:
                flag = flag + 1
                return ent
        if flag != 0:
            raise KeyError("Key is not valid")
        #try:
        #    for ent in self._entrySet:
        #        if ent.key == key:
        #            return ent
        #else:
        #    raise KeyError("Key is not valid")

    def getAsDictionary(self):
        res = {}
        for ent in self._entrySet:
            res[ent.key] = ent.value
        return res


if __name__ == "__main__":
    e1 = Entry(k=42, v="Answer to life, the universe, and everything.")
    print(e1)

    L1 = Lookup("Jack")


    L1.addEntry(e1)
    print(L1)
    #L1.addEntry(Entry(k=1,v=1))
    #print(L1)
    L1.removeEntry(e1)
    print(L1)
    #t = L1.getEntry(51)
    #print(t)
    #L1.removeEntry(e1)
    #res = L1.getAsDictionary()
    #print(res)