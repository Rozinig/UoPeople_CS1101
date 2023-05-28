# instructor defined function to print a line with a dot
def new_line():
    print(".")

# Instructor defined function that calls the new_line function to print three lines with dots
def three_lines():
	new_line()
	new_line()
	new_line()

# My Function that calls the three_lines function to print a total of nine lines with a dot
def nine_lines():
	three_lines()
	three_lines()
	three_lines()

#My function to print 25 lines with a dot. 9+9+3+3+1=25
def clear_screen():
	nine_lines()
	nine_lines()
	three_lines()
	three_lines()
	new_line()

#calls teh functions requested by the instructor with a heading for clarity.
print("Calling nine_lines")
nine_lines()
print("Calling clear_screen")
clear_screen()