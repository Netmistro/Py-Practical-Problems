# Write a program that generates 50 random numbers such that the first number is between 1 and 2
# The second is between 1 and 3
# The third is between 1 and 4, . . . , and the last is between 1 and 51.

from random import randint

# generate random number
for i in range(50):
    x = randint(1, i+1)
    print(x, end=' ')
