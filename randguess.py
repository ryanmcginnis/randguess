import random, os

number = 0

def C():
	os.system('clear')

def gRand():
	global number
	number = random.randint(1,10)
	return number

def g():
	try:
		guess = int(raw_input("Guess between 1 and 10: "))
		if guess < 11 and guess >= 1:
			if guess == number:
				C()
				print "Right!"
				gRand()
				g()
			else:
				C()
				print "Wrong! It was %d" % number
				gRand()
				g()
		else:
			C()
			print "Guess greater than 10 or less than 1."
			gRand()
			g()
	except KeyboardInterrupt:
		C()
		print "Quitting...\n"
		quit()
	except ValueError:
		C()
		print "Invalid input."
		gRand()
		g()
C()
gRand()
g()
