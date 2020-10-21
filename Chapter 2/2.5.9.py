# The Fibonacci numbers are the sequence below, where the first two numbers are 1,
# and each number thereafter is the sum of the two preceding numbers.
# Write a program that asks the user how many Fibonacci numbers to print and then prints that many.
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...

num = eval(input('How many fibonacci number to print? '))

firstNumber = 1

print(firstNumber)
for i in range(1, num):
    print(i)
