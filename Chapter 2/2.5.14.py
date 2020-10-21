# Use for loops to print a diamond like the one below
# Allow the user to specify how high the diamond should be
#      *
#     ***
#    *****
#   *******
#    *****
#     ***
#      *

# Calculate height and max width of diamond
height = eval(input("Enter height of diamond: "))
# Calculate number of rows for the iteration
rows = int((height-1)/2.0)
# starting number of stars
stars = 1
# number of spaces
space = rows - 1

# Top section of the diamond
for i in range(rows):
    print(' ' * (space), '*' * stars)
    # Decrease stars and spaces accordingly
    stars += 2
    space = space - 1
print('*' * height)

# Bottom section of the diamond
for i in range(rows):
    print(' ' * (space), '*' * stars)
    # Decrease stars and spaces accordingly
    stars -= 2
    space = space + 1
