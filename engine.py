#!/usr/bin/python3

import os
import pwd
import re
import socket
import subprocess
import sys

score = 0
points = []


def userAdded(user):
	global score
	person = 0
	for line in open('/etc/passwd'):
		if user in line:
			person = 1
	if person == 1:
		score = score+1
		points.append(f'Create user account {user}')
		return True
	else:
		return False

def userRemoved(user):
	global score
	person = 0
	for line in open('/etc/passwd'):
		if user in line:
			person = 1
	if person == 0:
		score = score+1
		points.append(f'Removed unauthorized user {user}')\
		return True
	else:
		return False

def groupAdded(group):
	global score
	person = 0
	for line in open('/etc/group'):
		if group in line:
			person = 1
	if person == 1:
		score = score+1
		points.append(f'Added The Group {group}')
		return True
	else:
		return False

def groupRemoved(group):
	global score
	person = 0
	for line in open('/etc/group'):
		if group in line:
			person = 1
	if person == 0:
		score = score+1
		points.append(f'Removed The Group {group}')
		return True
	else:
		return False

def groupAddedTo(user, group):
	global score
	p = subprocess.Popen(f"cat /etc/group | grep {group}", shell=True, stdout=subprocess.PIPE)
	d = p.stdout.read()
	p.wait()
	if user in d:
		score = score+1
		points.append(f'Added {user} To The {group} Group')
		return True
	else:
		return False

def groupRemovedFrom(user, group):
	global score
	p = subprocess.Popen(f"cat /etc/group | grep {group}", shell=True, stdout=subprocess.PIPE)
	d = p.stdout.read()
	p.wait()
	if user not in d:
		score = score+1
		points.append(f'Removed {user} From The {group} Group')
		return True
	else:
		return False

def disableGuestAccount(file_path):
	global score
	if os.path.isfile(file_path):
		p = subprocess.Popen("cat "+file_path, shell=True, stdout=subprocess.PIPE)
		d = p.stdout.read()
		p.wait()
	if "allow-guest=false" in d:
		score = score+1
        points.append('Disabled Guest Account')
    	return True
    else:
    	return False

def updates():
	global score
	p = subprocess.Popen("cat /etc/apt/sources.list", shell=True, stdout=subprocess.PIPE)
	d = p.stdout.read()
	p.stdout.close()
	p.wait()
	if "http://us.archive.ubuntu.com/ubuntu" and "http://security.ubuntu.com/ubuntu" in d:
		score = score+1
		points.append("Install updates from important security updates")
		return True
	else:
		return False

def firewallCheck():
	global score
	p = subprocess.Popen("ufw status", shell=True, stdout=subprocess.PIPE)
	d = p.stdout.read()
	p.stdout.close()
	p.wait()
	if ' active' in d:
		score = score+1
		points.append('Enabled The Firewall')
		return True
	else:
		return False

def malwareCheck(file_path):
	global score
	if not os.path.isfile(file_path):
		score = score+1
		points.append('Removed Harmful File')
		return True
	else:
		return False

def packageInstalled(package):
	p = subprocess.Popen(f"dpkg -l | grep {package}", shell=True, stdout=subprocess.PIPE)
	d = p.stdout.read()
	p.stdout.close()
	p.wait()
	if d:
		return True
	else:
		return False

def packageRemoved(package):
	p = subprocess.Popen(f"dpkg -l | grep {package}", shell=True, stdout=subprocess.PIPE)
	d = p.stdout.read()
	p.stdout.close()
	p.wait()
	if not d:
		return True
	else:
		return False