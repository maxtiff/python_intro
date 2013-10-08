from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copy from {0} to {1}".format(from_file, to_file))

in_file = open(from_file)
indata = in_file.read()

print ("the input file is {0} bytes long".format(len(indata)))

print ("Does the output file exist? {0}".format(exists(to_file)))
print ("Read, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print ("Finished")

out_file.close()
in_file.close()
