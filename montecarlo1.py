# Montecarlo to find pi	in 3D
# For a sphere of maximum volume inside a cube, (Volume of Sphere/Volume of Cube) = pi/6

from math import *
from time import *
from random import *

t0 = time()

count_inside = 0

for count in range(1, 100000):
	
    x = uniform(-1,1)
    y = uniform(-1,1)
    z = uniform(-1,1)
    
    d = sqrt ( x**2 + y**2 + z**2) 
    
    if d < 1 : count_inside += 1
	    
count += 1

r = 6.0 * count_inside / count 

print r

print time() - t0

