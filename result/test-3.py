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
            print alist[i]

class MyOtherClass():
    """Definition for MyOtherClass"""

    def __init__ (self):
        pass
    
    def methTwo(self):
        pass

if __name__=='__main__':
    c=MyClass()
    c.methTwo()
