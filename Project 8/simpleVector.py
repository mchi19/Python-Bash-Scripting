#! /bin/usr/env python3.4
import sys
import math

class Vector(object):
    def __init__(self, coordinates):
        temp = coordinates.split(" ")
        self.x = float(temp[0])
        self.y = float(temp[1])
if __name__ == "__main__":
    v1 = Vector("0.12 3.14")
    print(v1.x)
    print(v1.y)