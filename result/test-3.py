import os,sys,re,subprocess

def retEmptyList ():
    return []

class MyClass():
    """Definition for MyClass"""

    def __init__ (self):
        pass

    def methOne (self, l=[]):
        l.append('X')
        return l

    def prepNewList (self, l=retEmptyList()):
        l.append('Y')
        print l

    def checkList (self, alist):
        for i in range(len(alist)):

class MyOtherClass():
    """Definition for MyOtherClass"""

    def __init__ (self):
        pass

            print alist[i]

if __name__=='__main__':
    c=MyClass()
    c.methTwo()
