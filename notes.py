#crazy string from exam 2 

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