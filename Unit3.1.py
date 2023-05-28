def square():
    x=input('Please enter a number:')
    if x.isdigit():
        x=int(x)
        print('The square of {} is {}.'.format(x,x**2))
    else:
        print('That was not a number')
        square()

square()
