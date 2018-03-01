#! /bin/usr/env python3.4
import sys
import re
import math


class Transaction(object):
    def __init__(self, transType, value):
        if not transType == 'W': #or not transType == 'D':
            if not transType == 'D':
                raise ValueError("Error transType is not W or D")
        self.transType = transType
        self.value = value

class Person(object):
    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln

    def __str__(self):
        res = "{0} {1}".format(self.firstName, self.lastName)
        return res


class Account(object):
    def __init__(self, acntID, owner, balance):
        self.accountID = acntID
        self.owner = owner
        self.balance = balance
        self.minValue = 1000.0

    def __str__(self):
        if self.balance > 0:
            return "{0}, {1}, Balance = ${2:.2f}".format(self.accountID, self.owner, self.balance)
        else:
            temp = str(self.balance)
            temp = temp[1:]
            temp = float(temp)
            return "{0}, {1}, Balance = (${2:.2f})".format(self.accountID, self.owner, temp)

    def applyTransaction(self, trans):
        if trans.transType == 'D':
            #print("deposit")
            self.balance = self.balance + trans.value
            print("new balance after deposit: {0:.2f}".format(self.balance))
        else: #if trans.transType == 'W':
            chk = self.balance - trans.value
            if chk > 0:
                self.balance = self.balance - trans.value
                round(self.balance)
                if self.balance < self.minValue:
                    self.balance = self.balance - 10.00
                    round(self.balance)
            else: #if chk <= 0
                raise ValueError("You are unable to withdraw that amount from your account")
class Bank:
    def __init__(self):
        self.accounts = {}
    def createAccount(self, fn, ln, aID):
        p = Person(fn, ln)
        #a = Account(aID, p, 500.00)
        if aID not in self.accounts:
            self.accounts[aID] = "${0:.2f}".format(500.00)

    def applyTransaction(self, aID, trans):
        if aID in self.accounts:
            #print(type(self.accounts[aID]))
            temp = float(self.accounts[aID][1:])
            #print(temp)
            if trans.transType == 'D':
                self.accounts[aID] = "${0:.2f}".format(temp + trans.value)
            else:
                self.accounts[aID] = "${0:.2f}".format(temp + trans.value)


if __name__ == "__main__":
    t1 = Transaction('D', 150.0)
    t2 = Transaction('W', 100.0)
    print(t2.transType, t2.value)
    p1 = Person('John', 'Smith')
    #print(p1)
    a1 = Account("15487-79431", p1, 250.0)
    print(a1)

    print(a1.applyTransaction(t2))
    print(a1)

    B = Bank()
    print(B.accounts)
    B.createAccount("John", "Smith", "15487-79431")
    print(B.accounts)
    B.applyTransaction("15487-79431", t1)
    print(B.accounts)

