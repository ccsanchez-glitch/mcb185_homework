def oligo_temp(A, C, G, T):
	if A+ C + G + T <= 13:
		tm = (A + T)*2 + (G + C)*4 
		return tm 
	else:
		tm = 64.9 + 41*(G + C - 16.4)/(A + T + G + C)
		return tm 
		
print(oligo_temp(5, 7, 3, 4))
print(oligo_temp(8, 5, 2, 9))