def add(a, b):
	print ("Adding {0} + {1}".format(a, b))
	return a + b

def subtract(a,b):
	print ("Subtracting {0} - {1}".format(a, b))
	return a - b

def multiply(a,b):
	print ("Multiplying {0} * {1}".format(a, b))
	return a * b

def divide(a,b):
	print ("Dividing {0} / {1}".format(a, b))
	return a / b

print ("Let's do some math with just functions!")

age = add(20,7)
height = subtract(74,2)
weight = multiply(55,3)
iq = divide(100,2)

print ("Age: {0}, Height: {1}, Weight: {2}, IQ: {3}".format(age, height, weight, iq))
