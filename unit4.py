
#is_divisible function from section 6.4 in the book
def is_divisible(x, y):
	if x % y == 0:
		return True
	else:
		return False

# is_power function to check if a is a power of b
def is_power(a,b):
	# runs is_divisible to determined if a is divisible by b
	x=is_divisible(a,b)
	# if a is not divisible by b it returns false
	if not x:
		return False
	# check the base case of the second arguement being 1 if the first arguement is not
	elif b==1 and a!=1:
		return False
	#recursively runs the is_power function to drill all the way down
	elif not a==b:
		return is_power(a/b,b)
	#Returns true if nothing else catches which should just be if a is equal to b and is therefore a is a power of b
	else:
		return True

# runs required test statements
print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))