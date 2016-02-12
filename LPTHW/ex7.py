x = "There are %d types of people" % 10 # Assign a string to x using format operators
binary = "binary" # Assign a string to binary
do_not = "don't" # Assign a string to do_not
y = "Those who know %s and those who %s. " % (binary, do_not) # Assign a string to y using a format operators

print x # Print x
print y # Pring y

print "I said: %r." % x # Print line with format operator
print "I also said: '%s'." % y # Print line with format operator

hilarious = False # Assign a binary value to hilarious
joke_evaluation = "Isn't that joke so funny?! %r" # Assign a string to joke_evaluation with a format operator, and with the value to be chosen later.

print joke_evaluation % hilarious # Print joke_evaluation with hilarious formatted in

w = "This is the left side of..." # Assign string to w
e = "a string with a right side." # Assign string to e

print w + e # Print w then print e