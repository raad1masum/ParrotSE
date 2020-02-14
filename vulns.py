#!/usr/bin/python3

from engine import *

pointsTotal = 0

def gainPoints(points):
	global pointsTotal

	pointsTotal = points + pointsTotal

	f = open("scoreTMP.txt", "w")
	f.write(str(pointsTotal))
	f.close()

def gainVuln(description, pointValue):
	global vulnReport

	gainPoints(pointValue)
	vulnReport = description + ' - ' + pointValue + ' pts<br>'

	f = open("reportTMP.txt", "w")
	f.write(str(vulnReport))
	f.close()

############################################
#										   #
#  	  Begin Vulnerability Configuration    #
#										   #
############################################

if checkUpdate():
	gainPoints(3)

if userAdded('administrator'):
	gainPoints(3)

if userRemoved('administrator'):
	gainPoints(3)

if lineInFile('allow-guest=false','/etc/lightdm/lightdm.conf'):
	print('worked')

############################################
#										   #
#	   End Vulnerability Configuration     #
#										   #
############################################

print('Points: ' + str(pointsTotal))