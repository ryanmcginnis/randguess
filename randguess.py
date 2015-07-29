import random

# bug: no way out of exceptions when non-numeric input is received

number = 0

def gRand():
	global number
	number = random.randint(1,10)
	return number

def g():
	guess = input("Guess between 1 and 10: ")
	guess = int(guess)
	if isinstance(guess, int): # check if input is numeric
		if guess < 11:
			if guess == number:
				print "Right!"
				gRand()
				g()
			else:
				print "Wrong! It was %d" % number
				gRand()
				g()
		else:
			print "Guess greater than 10."
			gRand()
			g()
	else:
		gRand()
		g()

gRand()
g()