import math

def my_sqrt(a):
	x=a
	while True:
		y = (x + a/x) / 2.0
		if y == x:
			return x
		x = y 


# the test_sqrt function takes the number of square roots to compute and does a while loop until that number
def test_sqrt(f):
	i=1
	while i<=f:
		v=my_sqrt(i)
		print('a = ',i,' | my_sqrt(a) = ',v,' | math.sqrt(a) = ',math.sqrt(i),' | diff = ',abs(v-math.sqrt(i)))
		i=i+1

test_sqrt(25)