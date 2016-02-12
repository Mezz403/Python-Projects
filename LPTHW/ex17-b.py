from sys import argv

script, filename = argv

txt = open(filename)

print "Here is the filename: %s" % filename
print "Here are the contents: "
print txt.read()

txt.close()
