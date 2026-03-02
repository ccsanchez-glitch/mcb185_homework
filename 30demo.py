# structure for reading a file line-by-line

fp = open(path) 	#open function creates a file pointer, path can be rel or abs
for line in fp:
	do_something_with(line)
fp.close()			#closes the file, forgetting to close it can cause errors 

# alternate path for reading files 

with open(path) as fp:	#no close function bc python will automatically close it 
	for line in fp: 
		do_something_with(line)
		

# open a compressed file 

import gzip 
with gzip.open(path, 'rt') as fp: 
	for line in fp:
		print(line, end=' ')

