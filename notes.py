#crazy string from exam 2 
'''
def crazy(s):
	cs = ''
	for i, c in enumerate(s):
		if i % 2 == 0: 	cs += c.upper()
		else: 			cs += c.lower()
	return cs
	
	
filename = sys.argv[1]	
with open(filename) as fp: 
	for line in fp: 
		crazyline = crazy(line)
		print(crazyline)
		
		
#another way to change the upper and lowercase 
		
def crazy(s):
	cs = []
	for i, c in enumerate(s):
		if i % 2 == 0: 	cs.append(c.upper())
		else: 			cs.append(c.lower())
	return ''.join(cs)
	
def crazy(s):
	cs = ''
	for i, c in enumerate(s):
		if i % 2 == 0: 	print(i, c.upper())
		else: 			print(i, c.lower())
	sys.exit()
	
def crazy(s):
	for i in range(len(s))
		if i % 2 == 0: 	print(i, s[i].upper())
		else: 			print(i, s[1].lower())
	sys.exit()
	
def crazy(s):
	sign = 1 
	for i in range(len(s)):
		if sign == 1: 	print(i, s[i].upper())
		else: 			print(i, s[1].lower())
	sys.exit()
	
	
	
# write a function anti that returns the antiparallel 

def anti(dna):
	rev = dna[::-1]
	comp = list()		# can also define empty list as a string []
	for nt in rev:
		if nt == 'A': comp.append('T')	#you append a list not a string
		elif nt == 'C': comp.append('G')	#if this was a string you would use +=
		elif nt == 'G': comp.append('C')
		elif nt == 'T': comp.append('A')
		else: sys.exit(f'unknown nt {nt}')
	return ''. join(comp)
	
seq = input('type sequence: ')
print(seq) 

#max string, longest string in a set of strings 

def longest_str(s):
	if len(s[0]) > len(s[1]) and len(s[0]) > len(s[2]):	print(s[0], len(s[0]))
	if len(s[1]) > len(s[2]): 							print(s[1], len(s[1]))
	else: 												print(s[2], len(s[2]))
	return 'the string', 9 


def longest_str(strings):
	longest = s[0]
	for s in strings[1:]:
		if len(s) > len(longest): longest = s
	return longest, len(longest)
	
strings = ['hello world', 'pi', '3.14159', 'mouserat']


# Write a function manhattan(X1, X2) that computes the Manhattan 
#distance between two lists of numbers.

# make two files of probabilities 
a = [0.25, 0.25, 0.25,0.25]
b = [0.4, 0.3, 0.2, 0.1]

def manhattan(X1, X2):
	distance = 0 
	for x1, x2 in zip(X1, X2):
		distance += abs(x1-x2)
	return distance
	
print(manhattan(a,b))


# 33 Write a function dkl(P, Q) that computes the Kullback-Leibler distance between 
# two histograms. You should check that P and Q are actually histograms and you should 
# do something about values of zero.

import math
b = [0.25, 0.25, 0.25,0.25]
a = [0.4, 0.3, 0.2, 0.1]

def dkl(P, Q):
	if not math.isclose(1.0, sum(P)): sys.exit('error')
	if not math.isclose(1.0, sum(Q)): sys.exit('error')
	distance = 0 
	for p, q in zip(P, Q):
		if p == 0: continue
		if q == 0: continue
		distance = p * math.log2(p/q)
	return -distance 

print(dkl(a, b))


# Write a function percent_id(s1, s2) that computes the percent identity 
# between two strings of equal length (e.g. a pairwise sequence alignment).

s1 = 'ACGATATACAGTACTA'
s2 = 'ACGATAGACAGTAGGG'

def pairwise_percent(s1, s2):
	diff = 0 
	for c1, c2 in zip(s1, s2):
		if c1 != c2: diff += 1
		return (1 - diff/(len(s1)))
	
print(pairwise_percent(s1, s2))


#jaccard index , need two files of lists 

import sys 

def get_list_from_file(filename):
	strings = []
	with open(filename) as fp:
		for line in fp:
			strings.append(line)
	return strings
			
def jaccard(f1, f2):
	X1 = get_list_from_file(f1)
	X2 = get_list_from_file(f2)
	unique_a = []
	unique_b = []
	shared = []
	for x1 in X1: 
		if x1 in X2:	 shared.append(x1)
		else: 			unique_a.append(x1)
	for x2 in X2: 
		if x2 not in X1: unique_b.append(x2)
	print(unique_a)
	print(unique_b)
	print(shared)
	return len(shared)/(len(shared) + len(unique_a) + len(unique_b)) 


file1 = sys.argv[1] 	#in terminal input nums1 
file2 = sys.argv[2] 	#in terminal input nums2 
print(jaccard(file1, file2))


# color name 

# 2/40/81 022851 aggie blue 
# 255/191/0 aggie gold 

import sys 

filename = sys.argv[1]
target_r = int(sys.argv[2])
target_g = int(sys.argv[3])
target_b = int(sys.argv[4])

min_distance = 1000
min_color = None

with open(filename) as fp:
	for line in fp:
		colornanme, hexvalue, rgbs = line.split()
		r, g, b = parts[2],split(',')
		distance = 0
		distance += abs(target_r - int(r))
		distance += abs(target_g - int(g))
		distance += abs(target_b - int(b))
		
		if distance < min_distance: 
			min_distance = distance 
			min_color = colorname 
	print(color, distance)


#complicated translating one 

import itertools 

def translate(seq):
	codons = [''.join(t) for t in itertools.product('ACGT', repeat=3)]
	trans = 'KNKNTTTTRSRSIIMIQHQHPPPPRRRRLLLLEDEDAAAAGGGGVVVV*Y*YSSSS*CWCLFLF'		
	
print(translate(''))
'''

import random 

inside = 0 
outside = 0 
while True:
	x = random.random()
	y = random.random()
	d = (x**2 + y**2)**0.5
	if d > 1:	outside += 1 
	else: 		inside += 1 
	
	print(4 * inside / (inside + outside))