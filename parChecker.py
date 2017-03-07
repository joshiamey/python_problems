from dataStructs.Stack import Stack

pairs = {'(':')','{':'}','[':']'}


def parChecker(arg):
	balanced = True
	s = Stack()

	for ch in arg:
		if ch in "({[" :
			s.push(ch)
		elif ch in ")}]":
			if s.isEmpty():
				balanced = False
				break
			else:
				top = s.pop()
				if pairs.get(top) != ch:
					balanced = False
					break
	return balanced


args = "[]"
print(parChecker(args))