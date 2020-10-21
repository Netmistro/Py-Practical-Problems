# Write a program that asks the user for a number of seconds and prints out how many minutes and seconds
# that is. For instance, 200 seconds is 3 minutes and 20 seconds.
# [Hint: Use the // operator to get minutes and the % operator to get seconds.]

seconds = eval(input("Enter number of seconds: "))
remainingSeconds = seconds % 60
minutes = (seconds - remainingSeconds) / 60

print('The number of minutes and seconds in ', seconds, ' seconds',
      ' is: ', minutes, ' minutes and ', remainingSeconds, ' seconds.')
