from dataStructs.Stack import Stack

def reverseStr(arg):
	s = Stack()
	
	for ch in arg:
		s.push(ch)

	ret = s.pop()
	while not s.isEmpty():
		ret += s.pop()

	return ret



print('Enter a string to reverse.')
string = str(input())
print('Entered string is ' + string)

print('\n reversed string is : ' + reverseStr(string))
