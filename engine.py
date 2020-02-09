import os
import pwd
import re
import socket
import subprocess
import sys

score = 0
points = []

def updates(topic,respository):
   global score
   p = subprocess.Popen("cat /etc/apt/sources.list", shell=True, stdout=subprocess.PIPE)
   d = p.stdout.read()
   p.stdout.close()
   p.wait()
   if respository in d:
      score = score+1
      points.append(topic+" Respository Added To Debian Package Lists")

def packageInstalled(package):
   p = subprocess.Popen("dpkg -l | grep " +package, shell=True, stdout=subprocess.PIPE)
   d = p.stdout.read()
   p.stdout.close()
   p.wait()
   if d:
       return True
   else:
       return False

def packageRemoved(package):
   p = subprocess.Popen("dpkg -l | grep " +package, shell=True, stdout=subprocess.PIPE)
   d = p.stdout.read()
   p.stdout.close()
   p.wait()
   if not d:
       return True
   else:
       return False