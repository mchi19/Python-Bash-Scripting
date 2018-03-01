#! /bin/usr/env python3.4

import math
import sys

class Rectangle(object):
    def __init__(self, ll, ur):
        if (ll[0] < ur[0]) and (ll[1] < ur[1]):
            self.llPoint = ll
            self.urPoint = ur
        else:
            raise ValueError("Lower-Left point must be less than Upper-Right point.")

    def isSquare(self):
        if (self.urPoint[0] - self.llPoint[0]) == (self.urPoint[1] - self.llPoint[1]):
            return True
        return False

    def isPointInside(self, point):
        if (self.llPoint[0] < point[0] < self.urPoint[0]) and (self.llPoint[1] < point[1] < self.urPoint[1]):
            return True
        return False

    def intersectsWith(self, rect):
        p1 = (rect.llPoint[0], rect.urPoint[1])
        p2 = (rect.llPoint[1], rect.urPoint[0])
        if (self.isPointInside(rect.llPoint) == True) or (self.isPointInside(rect.urPoint) == True) or (self.isPointInside(p1) or (self.isPointInside(p2))):
            return True
        return False

if __name__ == "__main__":
    ### part 1
    ll = (1,2)
    ur = (5,6)
    r1 = Rectangle(ll, ur)

    ### part 2
    print(r1.isSquare())

    ### part 3
    pt = (1,3)
    print(r1.isPointInside(pt))

    ### part 4
    ll1 = (0,0)
    ur1 = (2,3)
    r2 = Rectangle(ll1, ur1)
    print(r1.intersectsWith(r2))