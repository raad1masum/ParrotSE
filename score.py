import time
import random

points = random.randint(1,101)

f = open("scoreTMP.txt", "w")

def scoring():
	for x in range(100):
	  time.sleep(2)
	  points = random.randint(1,101)
	return points

f.write(str(points))
f.close()

exec(open("report.py").read())