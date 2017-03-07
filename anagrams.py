
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
           

    return list(set(perms))


def findanagram(haystack,needle):
    indices = []
    anagrams = permute(needle)

    for anagram in anagrams:
        reg = re.compile(anagram)
        for m in re.finditer(reg,haystack):            
            print(m.start())
            print(m.group())
            indices.append(m.start())

    indices.sort()
    return indices

str1 = "maranaganagram"
str2 = "anagram"

result = findanagram(str1,str2)

print(result)