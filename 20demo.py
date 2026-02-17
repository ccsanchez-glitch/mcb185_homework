import math 

s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = " don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')

print(len(s))
print(chr(65))
print(ord('a'))

print(s.count(s1))

print(s.upper())
print(s)

print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i')) #prints hell wild

print(f'{math.pi}') 			# does nothing special 
print(f'{math.pi:.3f}')			# 3 fixed digits after decimal 
print(f'{1e6 * math.pi:e}')		# exponent notation 
print(f'{"hello world":>20}')	# right justify with space filler
print(f'{"hello world":.>20}')	# right justify with dot filler 
print(f'{20:<10}{10}')			# left justify 

seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq: 
	print(nt, end='')
print()			# prints code without % sign at the end 

for i in range(len(seq)):
	print(i, seq[i])
	
s = 'ABCDEFGHIJ'
print(s[0:5])				# prints letters in index 0,1,2,3,4
print(s[0:8:2])				# prints letters in index 0,2,4,6,8
print(s[0:5], s[:5])		# both ABCDE
print(s[5:len(s)], s[5:])	# both FGHIJ

print(s, s[::], s[::1], s[::-1])	# s[::-1] will print the slice backwards

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
	codon = dna[i: i+3]		# need to do i+3 as the before endpoint or else the codons will be two letters
	print(i, codon)
	
tax = ('Homo', 'sapiens', 9606)	#construct tuple
print(tax)						# note the parenthesis in the output 
print(tax[0])
print(tax[::-1])

nts ='ACGT'
for i in range(len(nts)):
	print(i, nts[i]) 
	
for i, nt in enumerate(nts):
	print(i, nt)
	
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])
	
for nt, name in zip(nts, names):
	print(nt, name)
	
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
	
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts 
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ABCDEFGHIJKLMNOPQRSTU'
print(alph)
aas = list(alph)
print(aas)

text = 'good day           to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))
# print('index Z?', alph.index('Z'))		will give an error

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))	# prints a -1 because it cannot be found 

# Write a function that returns the minimum value of a list.

def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val 
	return mini
	
# Write a function that returns both the minimum and maximum values of a list.

def minimax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals: 
		if val < mini: mini = val 
		of val > maxi: maxi = val 
	return mini, maxi 
	
