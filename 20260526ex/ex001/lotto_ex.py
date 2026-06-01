# quiz) 로또 당첨게임
import random

userNums = []
randNums = []
collect = []

def setUNumbers(ns):     # setter  set + UNumbers  리스트를 담아두는 또는 저장하는 역할
    global userNums
    userNums = ns

def getUNumbers():     # getter  get + UNumbers   리스트에 담아둔 아이템 가져오는 역할
    return userNums

def setRNumbers():
    global randNums

    randNums = random.sample(range(1, 46),6)

def getRNumbers():
    return randNums

def compareNumbers():
    global userNums
    global randNums
    global collect


    collect = []

    for item in userNums:
        if randNums.count(item) != 0:
           collect.append(item)

    return collect