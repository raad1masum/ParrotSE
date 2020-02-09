import os
import pwd
import re
import socket
import subprocess
import sys

score = 0
points = []


def programInstalled(program):
   p = subprocess.Popen("dpkg -l | grep " +program, shell=True, stdout=subprocess.PIPE)
   d = p.stdout.read()
   p.stdout.close()
   p.wait()
   if d:
       return True
   else:
       return False

def programRemoved(program):
   p = subprocess.Popen("dpkg -l | grep " +program, shell=True, stdout=subprocess.PIPE)
   d = p.stdout.read()
   p.stdout.close()
   p.wait()
   if not d:
       return True
   else:
       return False