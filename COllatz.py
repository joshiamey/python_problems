# Program to generate Collatz sequence.

def Collatz(number):

	if (number % 2 == 0):
		print (number // 2)
		return (number // 2)
	else:
		print ( 3 * number + 1)
		return (3 * number + 1)


print(' Enter a random integer greater than 1 to generate Collatz sequence: ')
try:
	no = int(input())

	while(no != 1):
		no = Collatz(no)

except ValueError:
	print ('Invalid type entered please enter an integer.')
