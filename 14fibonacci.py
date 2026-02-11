"""
A classic programming interview question is to write a program that 
reports the first 10 numbers from the Fibonacci sequence: 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34. This is a tricky problem. You need
 to initialize and keep track of 2 previous values.
""" 

def fib(n): 
	first = 0 
	second = 1 
	print(first)
	print(second)
	third = first + second 
	print(third)
	for i in range(3, n): 
		first = second 
		second = third 
		third = first + second 
		print(third)
	

print(fib(10))
