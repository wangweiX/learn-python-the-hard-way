from sys import argv

script, filename = argv

txt = open(filename,"rb",10)

print "Here's your file %r:" % filename
print "Name of the file:", txt.name
print "Closed or not : ", txt.closed
print "Opening mode : ", txt.mode
print "Softspace flag : ", txt.softspace
print txt.read()
txt.close()

file_again = raw_input("Type the filename again: ")

txt_again = open(file_again)

#raw_input("txt_again content:")
raw_input(txt_again.read(10))
txt_again.close()
