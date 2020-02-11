#!/usr/bin/python3

from engine import *

pointsTotal = 0

def gainPoints(points):
	pointsTotal = pointsTotal + points

if checkUpdate():
	gainPoints(3)