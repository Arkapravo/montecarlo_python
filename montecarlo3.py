# Montecarlo method to find pi	in 3D
# A cube of maximum volume is embedded inside a sphere of unit radius, (Volume of Sphere/Volume of Cube) = 0.8660*pi

# count is a count of the number of random points inside the sphere
# count_inside is a count of the number of random points inside the cube

from math import *
from time import *
from random import *

t0 = time()

count_inside = 0
count = 0

for BLAH in range (1, 100000) :

	x = uniform(-1,1)
	y = uniform(-1,1)
	z = uniform(-1,1)
	
	if -3**(-0.5) < x < 3**(-0.5): 
		if -3**(-0.5) < y < 3**(-0.5): 
			if -3**(-0.5) < z < 3**(-0.5):
				count_inside +=1
			
	if (x**2 + y**2 + z**2) < 1**2 :
		count +=1			
		
r = (2.0/sqrt(3)) * count / count_inside 

print r

print time() - t0
