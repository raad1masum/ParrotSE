#!/usr/bin/python3

from engine import *

pointsTotal = 0

def gainPoints(points):
	pointsTotal = points + pointsTotal

if checkUpdate():
	gainPoints(3)