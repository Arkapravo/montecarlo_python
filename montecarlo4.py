# Montecarlo method to find pi	in 3D
# A cylinder is constructed such that a unit cube just fits inside it, (Volume of Cylinder/Volume of Cube) = pi/2

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
	
	if -2**(-0.5) < x < 2**(-0.5): 
		if -2**(-0.5) < y < 2**(-0.5): 	
			if -2**(-0.5) < z < 2**(-0.5): 
				count_inside +=1
			
	if (x**2 + y**2) < 1**2 :
		if  -2**(-0.5) < z < 2**(-0.5): 
			count +=1			
		
r = 2.0 * count / count_inside 

print r

print time() - t0
