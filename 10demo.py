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


#strings 

s = 'hello world'
print(s, type(s))

a=5
b=3
if a == b: 
	print('a equals b')
	
if a == b:
	print('a equals b')
print(a, b)
	
def is_even(x):
	if x % 2 == 0: return True
	return False 
	
print(is_even(2))
print(is_even(3))

c = a == b 
print(c)
print(type(c))
	
	
if a < b: 
	print('a < b')
elif a >b: 
	print('a > b')
else:
	print('a == b')
	
if		a < b: 	print('a < b')
elif 	a > b: 	print('a > b')
else: 			print('a == b')

if		a < b: 	print('a < b')
elif 	a >= b: print('a >= b')
elif 	a == b:	print('this will never print!')


a = 0.3 
b = 0.1 * 3 
if   a < b: print('a < b')
elif a > b: print('a > b')
else: 		print('a ==b')

print(abs(a-b))
if abs(a-b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

#None type, there is no return command in the function 

def silly(m, x, b):
	y = m * x + b 
	
print(silly(2, 3,4))


#mismatch type error 

a = 1
s = 'G'
# cannot compare an integer to a string 

def is_integer(n): 
	if n % 1 == 0: return True
	return False
	
print(is_integer(4.5))
print(is_integer(4))

def is_probability(p): 
	if p >= 0 and p <= 1: return True 
	return False 
	
print(is_probability(1.5))
print(is_probability(0.5))

def dna_completment(nt):
	if nt == 'A': return 'T'
	if nt == 'C': return 'G' 
	if nt == 'G': return 'C' 
	if nt == 'T': return 'A'
	return 'None'
	
print(dna_completment('T'))
print(dna_completment('H'))


def max3(a, b, c):
	if a > b and a > c: return a
	if b > c: 			return b 
	return c 
	
print(max3( 3, 5, 7))
