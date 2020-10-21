
# Use a for loop to print an upside down triangle like the one below
# Allow the user to specify how high the triangle should be
# ****
# ***
# **
# *

numberOfRows = eval(input("Enter number of rows "))

for i in range(numberOfRows, 0, -1):
    print('*' * i)
