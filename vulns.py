#!/usr/bin/python3

import os
from engine import *

pointsTotal = 0 # total current points

possiblePoints = 100 # max possible points

vulnTotal = 0 # total current vulns

possibleVulns = 30 # max possible vulns

os.system('> reportTMP.txt')

def gainPoints(points):
	global pointsTotal

	pointsTotal = points + pointsTotal

	f = open("scoreTMP.txt", "w")
	f.write(str(pointsTotal))
	f.close()

def vuln(description, pointValue):
	global vulnReport
	global pointReport
	global vulnTotal

	vulnTotal += 1

	gainPoints(pointValue)
	vulnReport = str(description) + ' - ' + str(pointValue) + ' pts<br>'
	pointReport = '<h2>' + str(pointsTotal) + ' out of ' + str(possiblePoints) + ' points received</h2>'
	pointReport2 = '<h3>' + str(vulnTotal) + ' out of ' + str(possibleVulns) + ' scored security issues fixed, for a gain of ' + str(pointsTotal) + 'points:</h3>'

	f = open("reportTMP.txt", "a")
	f.write(str(pointReport))
	f.write('<p>')
	f.write('</p>')
	f.write(str(pointReport2))
	f.write('<p>')
	f.write(str(vulnReport))
	f.close()

def generateReport():
	os.system('> ScoringReport.html')
	os.system('cat HEADER.html >> ScoringReport.html')
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