import math
import sys

stack = []

def plus(a, b):
   return a + b

def minus(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   return a / b

def power(a, b):
   return a ** b

def square(a):
   return a * a

def squareroot(a):
   return math.sqrt(a)

def log(a):
   return math.log(a)

def negate(a):
   return (-a)

binary_ops = {
       "+": plus,
       "-": minus,
       "*": multiply,
       "/": divide,
       "**": power,
}

unary_ops = {
       "n": negate,
       "s": square,
       "r": squareroot,
       "l": log,
}

def rpn(stack, token):
   if token in binary_ops and len(stack) >= 2:
      b = stack.pop()
      a = stack.pop()
      stack.append(binary_ops[token](a, b))
   elif token in unary_ops:
      a = stack.pop()
      stack.append(unary_ops[token](a))
   elif token == "p":
      print stack[len(stack) - 1]
   else:
      stack.append(float(token))

def main():
   lines = sys.stdin.readline()
   stack = []
   while lines != "":
      line = lines.strip().split()	
      i = 0
      while i < len(line):
         rpn(stack, line[i])
         i = i + 1
      lines = sys.stdin.readline()

if __name__ == "__main__":
   main()




#def minus(a, b):
   #return a - b

#def multiply(a, b):
   #return a * b

#def divide(a, b):
   #return a / b

#def power(a, b):
   #return a ** b


