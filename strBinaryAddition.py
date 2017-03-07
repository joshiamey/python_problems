def addStr(str1,str2):

    if len(str1) > len(str2):
        str2 = makeStrEqual(str2,len(str1))
    else:
        str1 = makeStrEqual(str1,len(str2))

    str3 = ""
    carryover = 0
    for i in range(len(str1)-1,-1,-1):
        op1 =  int(str1[i])
        op2 =  int(str2[i])
        tmp,carryover = add(op1,op2,carryover)
        str3 = tmp + str3       

    if carryover:
        str3 = str(carryover) + str3
        
    return str3

def makeStrEqual(st,Explength):
    tmp = st
    for i in range(Explength - len(st)):
        tmp = "0" + tmp
    
    return tmp

def add(i,j,carryover):
    #XOR 2 bits and the carryover if any
    result = i ^ j ^ carryover

    #new carryover will be "and" of two bits i,j "or" the previous carryover
    carryover = (carryover & i) | (carryover & j) | (i & j)

    return str(result),carryover


print(addStr("1010110111001101101000","1000011011000000111100110"))