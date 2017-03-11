from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
color = raw_input("Which is your favorite name? ")
print "So, your favorite name is %r" % color