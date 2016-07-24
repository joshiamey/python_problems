def commaCode(listRef):
	lastItem = listRef[-1]
	listRef[-1] = ' and ' + lastItem
	retStr = listRef[0]
	for i in range(1,len(listRef)):
		retStr = retStr + ',' + listRef[i] 

	return retStr


def main():
	list = ['apples ','oranges','grapes']

	print(commaCode(list))


main()