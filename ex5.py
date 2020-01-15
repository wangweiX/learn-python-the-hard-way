my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %r eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
print '%(language)s has %(#)03d quote types.' % {'language': "Python", "#": 2}

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print "Unsigned octal: %o" % -17
print "Unsigned decimal: %u" % -2.324
print "Unsigned hexadecimal (lowercase): %x" % 100
print "Unsigned hexadecimal (uppercase): %X" % 100
print "Floating point exponential format (lowercase). %e" % 23223223
print "Floating point exponential format (uppercase). %E" % 23223223
print "Floating point decimal format. %f" % 232.2222
print "Floating point decimal format. %F" % 232.2222
print "Same as \"e\" if exponent is greater than -4 or less than precision, \"f\" otherwise. %g" % 23223223
print "Same as \"E\" if exponent is greater than -4 or less than precision, \"F\" otherwise. %G" % 23223223
print "Single character (accepts integer or single character string). %c" % "w"