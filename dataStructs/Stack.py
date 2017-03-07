import sys
import re


class Stack:
	def __init__(self):
		self.items = []

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	def isEmpty(self):
		return (self.items == [])

	def size(self):
		return len(self.items)


def doStore(stack,test):

	for num in test.split():
		stack.push(num)

def printalternate(stack):

	alternates = []
	while not stack.isEmpty():
		alternates.append(stack.pop())
		if not stack.isEmpty():
			stack.pop()

	print(" ".join(alternates))


if len(sys.argv) == 2:
	s = Stack()
	test_cases = open(sys.argv[1], 'r')
	for test in test_cases:
		doStore(s,test)
		printalternate(s)

	test_cases.close()
else:
    print("Usage: python permutations.py filename")