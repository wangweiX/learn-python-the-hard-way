from sys import argv

script,input_file = argv

def print_all(f):
	print f.read()
	
def	rewind(f):
	f.seek(0)

# “The readline() function returns the \n that's in the file at the end of that line.”
def print_a_line(line_count,f):
	print line_count,f.readline()
		
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"
current_line = 1
print_a_line(current_line,current_file)

current_file.seek(2)

current_line += 1
print_a_line(current_line, current_file)

current_file.seek(3)

current_line += 1
print_a_line(current_line,current_file)