# 10demo.py by Christina Sanchez 

import math 
 
print ('hello again') #greeting 
 
"""
 This is a 
 multi-line 
 comment 
""" 

print(1.5e-2)
print(math.ceil(53))
print(math.floor(65))
print(math.log(math.e))
print(math.log2(8))
print(math.log10(1000))
print(math.sqrt(100))
print(math.pow(2,4))
print(2**4) 
print(math.factorial(3))

print('numbers arent real')
print(0.1*1)
print(0.1*3)

#Pythagorus 
a=3 						#side of a triangle
b=4							#side of a triangle 
c=math.sqrt(a**2 + b**2)	#hypotenuse
print(c)

print(type(a), type(b), type(c), sep=',', end='!\n')

def pythagorus(a, b): return math.sqrt(a**2 + b**2)
	
print(pythagorus(5, 12))


def circle_area(r): return math.pi * r**2 
def rectangle_area(w, h): return w * h 
print(rectangle_area(10, 15))

def triangle_area(w, h): return rectangle_area(w, h)/2


def tempf_c(f): return (f-32)*(9/5)
print(tempf_c(32))

def mphtokph(m): return m * 1.60934
print(mphtokph(50))

def distance_two_points(x1, y1, x2, y2): 
	dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
	return dist 
	
print (distance_two_points(2, 3, 5, 7))