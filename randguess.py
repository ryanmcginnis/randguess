import random, os

number = 0

def C():
	os.system('clear')
	
def isNumber(guess):
	try:
		int(guess)
		return True
	except ValueError: 
		return False
		
def signal_handler(signal, frame):
    sys.exit

def gRand():
	global number
	number = random.randint(1,10)
	return number

def g():
	try:
		guess = raw_input("Guess between 1 and 10: ")
		if isNumber(guess) == True:
		# if isinstance(guess, int): # check if input is numeric
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
		elif isNumber(guess) == False:
			C()
			print "Invalid input."
			gRand()
			g()
	except KeyboardInterrupt:
		C()
		quit()
C()
gRand()
g()
