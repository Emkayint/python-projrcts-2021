def nums(x):
	for i in range(x):
	    print(i)
	    # return
nums(10)

print('\n')

cubes = [i**3 for i in range(5)]
print (cubes)

num = (55, 44, 33, 22)
print(max(min(num[:2]),abs(-42)))

print ('\n')

def fib(x):
	if x == 0 or x== 1:
		return 1
	else:
		return fib(x-1) + fib(x -2)
print (fib(4))
