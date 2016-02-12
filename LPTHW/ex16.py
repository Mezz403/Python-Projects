from sys import argv # Unpack arguments entered by the user

script, filename = argv # unpack entered arguments into script and filename

txt = open(filename) # open the provided filename and assign to txt

print "Here's your file %r: " % filename # display filename to user
print txt.read() # print the contexts of the file to screen

print "Type the filename again:" # ask for the filename again
file_again = raw_input("> ") # save user input to variable

txt_again = open(file_again) # open the file

print txt_again.read() # print contents of file to screen

txt.close()
txt_again.close()