from math import *

def combination (n,r):
    return factorial(n)/(factorial(n-r)*factorial(r))

def permutaion (n,r):
    return combination(n,r)*factorial(r)

def expTaylor (x,n):
    temp=0
    num=0
    while temp<=n:
        num=num+((x**temp)/factorial(temp))
        temp=temp+1
    return num

def expCal (x,n):
    return ((1+(1/n))**n)**x

def expErr (x,n):
    return expTaylor(x,n)-expCal(x,n)

def printErr (x,n):
    temp=1
    while temp<=n:
        print(expErr(x,temp))
        temp=temp+1
