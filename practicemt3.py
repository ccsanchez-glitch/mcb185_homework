'''
#41 Write a program print_matrix.py <alphabet> <plus> <minus> 
#that displays a simple scoring matrix for matches and mismatches. 
#The program must have the alphabet and scores as command line 
#arguments. Given the command line shown, the output should match 
#exactly.

import sys 

alph = sys.argv[1]
mat = sys.argv[2]
mis = sys.argv[3]

print(' ', end=' ') 			#adds a space to the beginning line 

for nt in alph: 				#prints the heading letters 
	print(nt, end='  ')
print()							#ends the line 

for nt1 in alph: 
	print(nt1, end=' ')			#prints the letters vertically
	for nt2 in alph: 			#prints the numbers for miss or match
		if nt1 == nt2: print(mat, end=' ')
		else: print(mis, end=' ')
	print()						#ends the line 
	

#42 Write a program triples.py <n> that finds all Pythagorean 
#Triples with sides from 1 to n (e.g. 100). There should be no 
#duplicates. For example, 3-4-5 is a Pythagorean Triple, 
#but 4-3-5 is really the same thing and should not be reported.

for a in range(1, 100):
	for b in range(a+1, 100):
		c = (a**2 + b**2)**0.5
		if c % 1 != 0: continue
		print(a, b, int(c))
		
#43 Write a program birthday1.py <c> <n> that simulates the 
#birthday paradox (the probability that two people in a classroom 
#have the same birthday is > 50% once the class size is 23 or more). 
#Use a list for the people, not the calendar. c and n represent 
#the size of the calendar (e.g. 365) and number of people (e.g. 23).

import sys 
import random

cal = int(sys.argv[1])
num = int(sys.argv[2])

shared = False 
birthdays = list()

for a in range(num):
	birthdays.append(random.randint(0, cal-1))
for i in range(num):
	for j in range(i+1, num):
		if birthdays[i] == birthdays[j]:
			shared = True
			
if shared:		print('hooray')
else:			print('not this time')


#44 Write a program birthday2.py <c> <n> as before but use a list 
#for the calendar, not the people.

import sys
import random 

cal = int(sys.argv[1])
num = int(sys.argv[2])

calendar = [0] * cal
shared = False 

for _ in range(num):
	date = random.randint(0, cal-1)
	calendar[date] += 1 
	
for date in range(cal):
	if calendar[date]  > 1: shared = True 
	
if shared:		print('hooray')
else:			print('not this time')


#45 Write a function polya(dna) that returns the length of the 
#longest stretch of As in a dna sequence.

seq = 'ACGTAAAATAAA'
print(seq)
max_run = 0 
max_pos = None
i = 0
while i < len(seq):
	if seq[i] == 'A': 
		run_start = i
		run_len = 1
		for j in range(i+1, len(seq)):
			if seq[j] == 'A': run_len += 1
			else: break 
		i = j 
		if run_len > max_run: 
			max_run = run_len 
			max_pos = run_start
		i += 1
print(max_run, max_pos)
'''

#46 Write a program char_count.py that prints out the character 
#count of each character in a file. Invisible characters should 
#be displayed by their ASCII value rather than the character.

s = 'hello	this is fun!'
characters = []
char_count = []

for c in s: 
	if c not in characters:
		print('first time seeing', c)
		characters.append(c)
		char_count.apppend(1)
	else: 
		print('seen', c, 'before, adding 1')
		idx = characters.index(c)
		char_count[idx] += 1
		
for c, n in zip(characters, char_count):
	if ord(c) <= 32: 	print(ord(c), n)
	else:				print(c, n)