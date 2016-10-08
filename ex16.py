from sys import argv
# Must provide a filename with input in command line
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# If CTRL-C is clicked, exit out of file, else proceed
raw_input("?")

print "Opening the file..."
target = open(filename, 'w') # open in writing mode

print "Truncating the file. Goodbye!"
target.truncate() # truncate file

print "Now I'm going to ask you for three lines."
# Input all the lines to be written
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# Write all the lines
target.write(line1 + '\n' + line2 + '\n' + line3)


print "And finally, we close it."
target.close() # close the file