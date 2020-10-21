# Use a for loop to print a box like the one below
# Allow the user to specify how wide and how high the box should be
# *******************
# *                 *
# *                 *
# *******************

cols = eval(input('Enter number of cols: '))
rows = eval(input('Enter number of rows: '))

print('*' * cols)
for i in range(rows-2):
    print('*', ' ' * (cols-4), '*')
print('*' * cols)
