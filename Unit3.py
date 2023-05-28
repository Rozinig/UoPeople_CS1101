#Countdown function from the book
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

#Countup function: counts up from a negative number to zero and sayes Blastoff
def countup(n):
    if n>=0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)

#Asks the user for what number the user would like to start a count from and stores it as an integer
n=int(input('What number will the count start from? \n'))

print('Starting the count!')

#If the number is greater than zero the program will run countdown
#and if less than zero will run countup
if n > 0:
    countdown(n)
else:
    countup(n)
