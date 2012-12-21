# Montecarlo to find pi	in 2D
# For a square of maximum area inside a circle, (Area of Circle/Area of Square) = 2*pi

from math import *
from time import *
from random import *

t0 = time()

count_inside = 0
count = 0

for BLAH in range (1, 100000) :

	x = uniform(-1,1)
	y = uniform(-1,1)
	
	if -2**(-0.5) < x < 2**(-0.5): 
		if -2**(-0.5) < y < 2**(-0.5): 			
			count_inside +=1
			
	if (x**2 + y**2) < 1**2 :
		count +=1			
		
r = 2.0 * count / count_inside 

# error = (abs(pi - r)/pi) * 100

print r
# print error
print time() - t0
