#!/usr/bin/python3

from engine import *

pointsTotal = 0

def gainPoints(points):
	global pointsTotal
	pointsTotal = points + pointsTotal

if checkUpdate():
	gainPoints(3)

if userAdded('administrator'):
	gainPoints(3)

if userRemoved('administrator'):
	gainPoints(3)

if disableGuestAccount('/etc/lightdm/lightdm.conf'):
	print('worked')

print('Points: ' + str(pointsTotal))