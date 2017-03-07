def EuclidGCD(a,b):

    if b == 0:
        return a

    aprime = a % b

    return EuclidGCD(b,aprime)


print(EuclidGCD(357,234))