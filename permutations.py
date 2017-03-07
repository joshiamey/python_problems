
import re
import sys

def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]


def permute(string):

    if(len(string) <=1):
        return string
    list_str = list(string)
    perms= []
    for i in range(0,len(list_str)):            
        swap(list_str,i,0)        
        string = "".join(list_str)
        first = string[0]
        rem_str = string[1:len(string)]
        permutations = permute(rem_str)

        #Append the first character to the permuations of remaining string
        for s in permutations:
            perms.append(first+s)
           

    return perms


def print_permutations(perms):

    print(",".join(perms))


if len(sys.argv) == 2:

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:
        if re.search(r'[A-Za-z]',test):
            permutations = permute(test.strip())
            print_permutations(permutations)

    test_cases.close()
else:
    print("Usage: python permutations.py filename")