def multiply(a,b):
    prodStr = "0"
    addZero = 0
    for digit in reversed(a) :
        tmpStr = doMultiply(int(digit),b,addZero)
        prodStr = str(int(prodStr)+int(tmpStr))
        addZero += 1

    return prodStr

def doMultiply(i,c,addZero):
    carry = 0
    res = ""
    for digit in reversed(c):
        x = (i * int(digit)) + carry
        y = x % 10
        carry = int(x / 10)
        res = str(y) + res
    
    if carry:
        res = str(carry) + res

    for i in range(addZero):
        res = res + "0"

    return res


print(multiply("311","31"))