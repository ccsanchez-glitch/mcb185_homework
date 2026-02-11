#wouldnt allow someone to type their own sequence 

def oligo_temp(A, C, G, T):
	if A+ C + G + T <= 13:
		tm = (A + T)*2 + (G + C)*4 
		return tm 
	else:
		tm = 64.9 + 41*(G + C - 16.4)/(A + T + G + C)
		return tm 
		
print(oligo_temp(5, 7, 3, 4))
print(oligo_temp(8, 5, 2, 9))

# allow input from terminal 

import sys 
print(sys.argv[1])
c = sys.argv[1], count('C')
g = sys.argv[1], count('G')

def tm(s):
	s = s.upper()
	a = s.count('A')
	c = s.count('C')
	g = s.count('G')
	t = s.count('T')
	if len)(s) != a + c + g + t: sys.exit('error in sequence')
	
	if len(s) <= 13:
		return (a + t) * 2 + (c + g) * 4
	else: 
		return 64.9 + 41 * (g + c - 16.4) / (a + t + g + c) 

seq = sys.argv[1]
print(tm(seq))

