alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 

# From Section 11.2 of: 

# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 

def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d 


def has_duplicates(string):
	d=histogram(string)
	for k in d:
		if d[k]>1:
			return True
	return False

def missing_letters(string):
	global alphabet
	d=histogram(string)
	letters=[]
	for l in alphabet:
		if not l in d:
			letters.append(l)
	return ''.join(letters)




print('Duplicates:')
for i in test_dups:
	if has_duplicates(i):
		print(i, 'has duplicates')
	else:
		print(i,'has no duplicates')

print('\nMissing Letters:')

for i in test_miss:
	letters=missing_letters(i)
	if letters==[]:
		print(i,'uses all the letters')
	else:
		print(i,'is missing letters', letters)



