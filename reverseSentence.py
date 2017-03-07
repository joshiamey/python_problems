import sys
import re

def reverse(sentence):
    list_str = sentence.split()
    retval = ""
    for i in range(len(list_str)-1,-1,-1):
        retval += list_str[i]
        retval += " "

    return retval


if len(sys.argv) == 2:

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:
        if re.search(r'[A-Za-z]',test):
            print(reverse(test))
         

    test_cases.close()
else:
    print("Usage: python permutations.py filename")