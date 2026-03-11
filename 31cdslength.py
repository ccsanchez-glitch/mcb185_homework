'''
zless ~/Code/MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz
 
 Create a program called 31cdslength.py that reports the lengths of protein-coding genes in the E. coli genome. The program will need to perform the following tasks as it reads each line of the file.

Skip over comment lines 
Find CDS features (or skip over all non-CDS features)
Extract the begin and end coordinates
Convert the coordinates to integers
Report the length of the CDS (end - begin + 1)
'''

import gzip 
import sys 


with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp: 
		if line[0] != '#':			#skip any lines that are comments
			words = line.split()	#split the file by spaces and save the info as words
			if words[2] == 'CDS':	#skip any lines that are not CDS 
				beg = int(words[3])	#extract the beginning coord
				end = int(words[4])	#extract the end coord
				print(end - beg +1) #report the length of the CDS (end - beg + 1)
 
 # use the continue command for the same task 
 
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue #continue will end the loop and start the next iteration at the beginning 
		words = line.split()
		if words[2] == 'CDS': continue 
		beg = int(words[3])
		end = int(words[4])
		print(end - beg + 1)