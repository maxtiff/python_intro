from sys import argv

script, filename = argv

print ("We're going to erase {0}".format(filename))
print ("If that's not cool, hit CTRL-C (^C).")
print ("Otherwise, just hit enter.")

input("What you gonna do?")

print ("Opening the file ...")
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

lines = [line1, line2, line3]

print ("Now I will write these shits to the file.")

for i in range(0,3):
	target.write(lines[i])
	target.write("\n")

print ("And then close it.")
target.close()
