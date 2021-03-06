#!/usr/bin/python3

import os
from engine import *

pointsEarned = 0 # total current points

pointsPossible = 100 # max possible points

vulnsEarned = 0 # total current vulns

vulnsPossible = 30 # max possible vulns

os.system('> reportTMP.txt')

def gainPoints(points):
	global pointsEarned

	pointsEarned = points + pointsEarned

	f = open("scoreTMP.txt", "w")
	f.write(str(pointsEarned))
	f.close()

def vuln(description, pointValue):
	global vulnReport
	global pointReport
	global vulnsEarned

	vulnsEarned += 1

	gainPoints(pointValue)
	vulnReport = str(description) + ' - ' + str(pointValue) + ' pts<br>'
	
	f = open("reportTMP.txt", "a")
	f.write(str(vulnReport))
	f.close()

def generateReport():
	pointReport = '<h2>' + str(pointsEarned) + ' out of ' + str(pointsPossible) + ' points received</h2>'
	pointReport2 = '<h3>' + str(vulnsEarned) + ' out of ' + str(vulnsPossible) + ' scored security issues fixed, for a gain of ' + str(pointsEarned) + ' points:</h3>'

	os.system('> ScoringReport.html')
	os.system('cat HEADER.html >> ScoringReport.html')

	f = open("ScoringReport.html", "a")
	f.write(str(pointReport))
	f.write('<p>')
	f.write('</p>')
	f.write(str(pointReport2))
	f.write('<p>')
	f.close()

	os.system('cat reportTMP.txt >> ScoringReport.html')
	os.system('cat FOOTER.html >> ScoringReport.html')

	f = open("scoreOLD.txt", "r")
	if pointsEarned > int(f.read()):
		os.system("notify-send 'ParrotSE' 'You Gained Points! :)'")
		os.system('aplay media/sounds/gain.wav > /dev/null 2>&1')
	f.close()
	
	f = open("scoreOLD.txt", "r")
	if pointsEarned < int(f.read()):
		os.system("notify-send 'ParrotSE' 'You Lost Points! :('")
		os.system('aplay media/sounds/alarm.wav > /dev/null 2>&1')
	f.close()

	f = open("scoreOLD.txt", "r")
	if pointsEarned == int(f.read()):
		os.system("notify-send 'ParrotSE' 'Your Points Did Not Change. :|'")
	f.close()

	os.system("cp scoreTMP.txt scoreOLD.txt")

############################################
#										   #
#  	  Begin Vulnerability Configuration    #
#										   #
############################################
'''
EXAMPLES:

if checkUpdate():
	vuln('Install updates from important security updates', 2)

if userAdded('administrator'):
	vuln('User administrator created', 3)

if userRemoved('hacker'):
	vuln('User hacker removed', 3)

if lineInFile('allow-guest=false','/etc/lightdm/lightdm.conf'):
	vuln('Guest Account Disabled', 3)
'''


############################################
#										   #
#	   End Vulnerability Configuration     #
#										   #
############################################

print('Points: ' + str(pointsEarned))
generateReport()