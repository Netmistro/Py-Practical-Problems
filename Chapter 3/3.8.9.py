# Write a program that asks the user for an hour between 1 and 12
# And for how many hours in the future they want to go
# Print out what the hour will be that many hours into the future
# An example is shown below:
# Enter hour: 8
# How many hours ahead? 5
# New hour: 1 O'clock

hour = eval(input("Please enter an hour between 1 and 12: "))
futureHours = eval(
    input("How many hours in the future would you like to go? "))

print("New Hour: ", (hour + futureHours) % 12, 'O Clock')
