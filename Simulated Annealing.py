import random
import math
import srtm
from math import e 

class FitnessFunction:
	def __init__(self):
		self.data = srtm.Srtm1HeightMapCollection()
	def __call__(self,x):
		try:
			elev = self.data.get_altitude(latitude=x[0],longitude=x[1])
		except srtm.exceptions.NoHeightMapDataException:
			elev = None
		return elev

f = FitnessFunction()

current = ((46.81819372475244, -92.08550938909693))

def find_neighbor(current):
	#Using the random.normalvariate function to find a neighbor of the current node.
	while(True):
		x = random.normalvariate(current[0],1.5)
		y = random.normalvariate(current[1],1.5)
		if(f((x,y)) is not None):
			return (x,y)

T = 1
while(T>0.00000000001):
	#Using a geometric decrement for the cooling schedule
	T = T*0.99
	for i in range(0,10000):
		x, y = find_neighbor(current)
		E = f((x,y)) - f(current)
		if E>0:
			current = (x,y)
		else:
			#If the new neighbor node isn't a better choice, we choose it with a probability of e^(E/T)
			if(random.random() <= math.pow(e,(E/T))):
				current = (x,y)

print(current)
print(f(current))
