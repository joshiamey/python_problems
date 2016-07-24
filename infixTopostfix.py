from dataStructs import Stack
import re

def isdigit(ch):
	return re.search("\d+",ch)

def isalpha(ch):
	return re.search("\w+",ch)


def infixToPostfix(args):
	precedence = {"*":3,"/":3,"+":2,"-":2,"(":1}


	opStack = Stack() #operator stack.

	outputList = []

	for token in args:
		if isdigit(token) or isalpha(token):
			print("appending : " + token)
			outputList.append(token)
		elif token in "(":
			opStack.push(token)
		elif token == ")":
				op = opStack.pop()
				while op != "(" :
					print("appending rar : " + op)
					outputList.append(op)
					op = opStack.pop()
		elif token in "*/+-":			
			while not opStack.isEmpty() and precedence[opStack.peek()] > precedence[token]:
				print("appending operator: " + token)
				outputList.append(opStack.pop())
			print("pushing : " + token)
			opStack.push(token)

		else:
			if not re.match('\s+',token):
				print("Invalid operator/operand encountered, quitting")
				break


	while not opStack.isEmpty():
		op = opStack.pop()
		print("After traversing is over appending : " + op)
		outputList.append(op)


	return " ".join(outputList)