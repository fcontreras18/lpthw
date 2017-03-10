from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)  # opens the first file
indata = in_file.read()  # copies the string into the variable

# print "The input file is %d bytes long" % len(indata)

# print "Does the output file exist? %r" % exists(to_file)  # does file exist?
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')  # creates new file
out_file.write(indata)  # writes the contents of to_file onto out_file

print "Alright, all done."

out_file.close()  # closes out_file
in_file.close()
