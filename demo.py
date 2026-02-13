"""
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

# february 12	
# birthday paradox , version 1 in discord 

import sys 
import random

people = int(sys.argv[1])
days = int(sys.argv[2])
iterations = int(sys.argv[3])

sames = 0 
for _ in range(iterations):
	calendar = [0] * days
	same_birthday = False
	for _ in range(people):
		bday = random.randint(0, days-1)
		if calendar[bday] == 1: 
			same_birthday = True 
			break
	 
	for v in calendar: 
		if v>1:
			same_birthday = True
	
	if same_birthday: sames += 1 
	
print(sames/iterations)











version 1
sames = 0 
for _ in range(iterations):
	classroom = []
	for i in range(people):
		birthday = random.randint(0, calendar-1)
		if birthday in classroom:
			same_birthday = True
			break
		classroom.append(birthday)

	same_birthday = False 
	classroom = ['A', 'B', 'C', 'D', 'E']
	for i in range(0, len(classroom)):
		for j in range(i+1, len(classroom)):	#start and i+1 for half matrix, i for half with major diagonal, start at zero for full  
			if classroom[i] == classroom[j]: same_birthday = True
		

	if same_birthday: sames +=1 

print(sames/iterations)
"""


