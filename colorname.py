# color name 

# 2/40/81 022851 aggie blue 
# 255/191/0 aggie gold 

import sys 

filename = sys.argv[1]
target_r = int(sys.argv[2])
target_g = int(sys.argv[3])
target_b = int(sys.argv[4])

min_distance = 1000
closest_color = None

with open(filename) as fp:
	for line in fp:
		colorname, hexvalue, rgbs = line.split()
		r, g, b = rgbs.split(',')
		distance = 0
		distance += abs(target_r - int(r))
		distance += abs(target_g - int(g))
		distance += abs(target_b - int(b))
		
		if distance < min_distance: 
			min_distance = distance 
			closest_color = colorname 
	print(closest_color, min_distance)
