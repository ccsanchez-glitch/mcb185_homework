def factorial(x):
	if x == 0: return 1 
	f = 1 
	for i in range(1, x+1):
		f = f * i 
	return f 
	
	
def is_prime(w):
	for d in range(2, w):
		if w % d == 0: return False
	return True

print(is_prime(14858678))

"""
def factorial(x):
	if x == 0: return 1 
	f = 1 
	for i in range(1, x+1):
		f = f * i 
	return f 
"""

import random 

for i in range(5):
	print(random.random())
	
#simulates rolling a six-sided die 

for i in range(3): #will give three outputs 
	print(random.randint(1,6))