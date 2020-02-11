#!/usr/bin/python3

import os
import re
import socket
import subprocess
import sys

score = 0
points = []


def lineInFile(line, file):
	try:
		with open(file) as f:
			if line in f.read():
				return True
			else:
				return False
	except:
		return False

def userAdded(user):
	try:
		global score
		person = 0
		for line in open('/etc/passwd'):
			if user in line:
				person = 1
		if person == 1:
			score = score+1
			points.append('Create user account ' +user)
			return True
		else:
			return False
	except:
		return False

def userRemoved(user):
	try:
		global score
		person = 0
		for line in open('/etc/passwd'):
			if user in line:
				person = 1
		if person == 0:
			score = score+1
			points.append('Removed unauthorized user ' +user)
			return True
		else:
			return False
	except:
		return False

def groupAdded(group):
	try:
		with open('/etc/group') as f:
			if group in f.read():
				return True
			else:
				return False
	except:
		return False

def groupRemoved(group):
	try:
		with open('/etc/group') as f:
			if group not in f.read():
				return True
			else:
				return False
	except:
		return False

def checkUpdate():
	try:
		with open('/etc/apt/sources.list') as f:
			if 'http://us.archive.ubuntu.com/ubuntu' and 'http://security.ubuntu.com/ubuntu' in f.read():
				return True
			else:
				return False
	except:
		return False

def malwareCheck(file_path):
	try:
		global score
		if not os.path.isfile(file_path):
			score = score+1
			points.append('Removed Harmful File')
			return True
		else:
			return False
	except:
		return False

def packageInstalled(package):
	try:
		p = subprocess.Popen("dpkg -l | grep " +package, shell=True, stdout=subprocess.PIPE)
		d = p.stdout.read()
		p.stdout.close()
		p.wait()
		if d:
			return True
		else:
			return False
	except:
		return False

def packageRemoved(package):
	try:
		p = subprocess.Popen("dpkg -l | grep " +package, shell=True, stdout=subprocess.PIPE)
		d = p.stdout.read()
		p.stdout.close()
		p.wait()
		if not d:
			return True
		else:
			return False
	except:
		return False