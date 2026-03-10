import sys 
import mcb185
# defline is an arbitrary variable we made to store the name of each fasta entry 

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline[:30], seq[:40], len(seq))