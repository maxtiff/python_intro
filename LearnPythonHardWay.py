def print_two(*args):
	arg1, arg2 = args
	print ("arg1: {0}, arg2: {1}".format(arg1, arg2))


def print_two_better(arg1, arg2):
	print ("arg1: {0}, arg2: {1}".format(arg1, arg2))

def print_one(arg1):
	print ("arg1: {0}".format(arg1))

def print_none():
	print ("I got nothin'.")

print_two('Travis', 'May')
print_two_better('Travis', 'May')
print_one('First!')
print_none()
