from sys import argv
# name of script, filename to open = argument variable
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# target = open a file, in this case .txt, and able to write
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()  # we use the truncate function to delete contents

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)  # writing the user input
target.write("\n")  # followed by a new line
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()  # now we close the text file
