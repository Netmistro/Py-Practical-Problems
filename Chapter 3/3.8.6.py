# 6. Write a program that asks the user to enter two numbers, x and y, and computes |x-y|/x+y.

from math import *

x = eval(input("Enter num1: "))
y = eval(input("Enter num2: "))

z = abs(x-y)/(x+y)

print(z)
