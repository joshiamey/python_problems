from dataStructs.Stack import Stack
import infixTopostfix

import re

operandStack = Stack()

class Calculator:
    def __init__(self):
        self.operandStack = Stack()

    
    def evaluate(self,op,a,b):
        result = None
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            result = a / b

        return result

    def evalPostFix(expr):

        for ch in expr:
            if re.search("\d+",ch) or re.search("\w+",ch):
                operandStack.push(ch)
            elif ch in "*/+-":
                op1 = int(operandStack.pop())
                op2 = int(operandStack.pop())
                res = evaluate(ch,op1,op2)
                operandStack.push(res)

        return operandStack.pop()


print(" Input an expression to calculate.")
expr = str(input())
print("Expression is : %s" % expr)

postFixExpr = infixTopostfix.infixToPostfix(expr)

print("Post fix Expression is : %s" % postFixExpr)

print("Calcualted value is: %d" % evalPostFix(postFixExpr))

