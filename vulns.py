#!/usr/bin/python3

import os
from engine import *

pointsTotal = 0

os.system('> reportTMP.txt')

def gainPoints(points):
	global pointsTotal

	pointsTotal = points + pointsTotal

	f = open("scoreTMP.txt", "w")
	f.write(str(pointsTotal))
	f.close()

def vuln(description, pointValue):
	global vulnReport

	gainPoints(pointValue)
	vulnReport = str(description) + ' - ' + str(pointValue) + ' pts<br>'

	f = open("reportTMP.txt", "a")
	f.write(str(vulnReport))
	f.close()

def generateReport():
	os.system('> ScoringReport.html')
	os.system('cat HEADER.html >> ScoringReport.html')
	os.system('cat <h2>83 out of 100 points received</h2> >> ScoringReport.html')
	os.system('cat <h3>0 penalties assessed, for a loss of 0 points:</h3> >> ScoringReport.html')
	os.system('cat <p> >> ScoringReport.html')
	os.system('cat </p> >> ScoringReport.html')
	os.system('cat <h3>36 out of 42 scored security issues fixed, for a gain of 85 points:</h3> >> ScoringReport.html')
	os.system('cat <p> >> ScoringReport.html')
	os.system('cat reportTMP.txt >> ScoringReport.html')
	os.system('cat FOOTER.html >> ScoringReport.html')

############################################
#										   #
#  	  Begin Vulnerability Configuration    #
#										   #
############################################

if checkUpdate():
	vuln('Install updates from important security updates', 2)

if userAdded('administrator'):
	vuln('User administrator created', 3)

if userRemoved('hacker'):
	vuln('User hacker removed', 3)

if lineInFile('allow-guest=false','/etc/lightdm/lightdm.conf'):
	vuln('Guest Account Disabled', 3)

############################################
#										   #
#	   End Vulnerability Configuration     #
#										   #
############################################

print('Points: ' + str(pointsTotal))
generateReport()