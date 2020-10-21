# Use a for loop to print a triangle like the one below
# Allow the user to specify how high the triangle should be
# *
# **
# ***
# ****

numberOfRows = eval(input("Enter number of rows for triangle: "))

for i in range(numberOfRows+1):
    print('*' * i)
