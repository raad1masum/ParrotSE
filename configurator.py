#!/usr/bin/python3

from engine import *

pointsTotal = 0

def gainPoints(points):
	global pointsTotal
	pointsTotal = points + pointsTotal

def vuln(description, pointValue):
	gainPoints(pointValue)

if checkUpdate():
	gainPoints(3)

if userAdded('administrator'):
	gainPoints(3)

if userRemoved('administrator'):
	gainPoints(3)

if lineInFile('allow-guest=false','/etc/lightdm/lightdm.conf'):
	print('worked')

f = open("scoreTMP.txt", "w")
f.write(str(points))
f.close()

print('Points: ' + str(pointsTotal))