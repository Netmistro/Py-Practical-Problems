# Use a for loop to print a box like the one below
# Allow the user to specify how wide and how high the box should be
# [Hint: print('*'*10) prints ten asterisks.]
#   *******************
#   *******************
#   *******************
#   *******************

widthOfBox = eval(input('Enter width of box: '))
heightOfBox = eval(input('Enter height of box: '))

for i in range(heightOfBox):
    print('*' * widthOfBox)
