
import math
import statistics
from functools import reduce
import time

def area(r):
    """Area of circle with radius r """
    return math.pi * (r ** 2)

radii = [2,5,7.1,0.3,10]

#Method 1: Direct method

areas = []

for r in radii:
    a = area(r)
    areas.append(a)

print(areas)

#Method 2: Use 'map' function

"""a = list(map(area, radii))

print(a)"""