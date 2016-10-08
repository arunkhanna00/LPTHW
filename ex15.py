from sys import argv
# Must provide a filename with input in command line
script, filename = argv

# Open the file
txt = open(filename)

print "Here's your file %r" % filename
# Read the file
print txt.read()

# Close the file
txt.close()

print "Type the filename again:"
# Receive the filename
file_again = raw_input("> ")

# Open the file
txt_again = open(file_again)

# Read the file
print txt_again.read()

# Close the file
txt_again.close()