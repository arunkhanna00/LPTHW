# Import modules
from sys import argv
from os.path import exists

# Must enter 2 file names in the command line
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# Open and read first file
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file) # check if file exists
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# Open and write data from first file into the second file
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

# Close both files
out_file.close()
in_file.close()
