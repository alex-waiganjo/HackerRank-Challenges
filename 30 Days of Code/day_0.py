#TASK
'''To complete this challenge, you must save a line of input from stdin to a variable, print Hello, World. on a single line, 
and finally print the value of your variable on a second line.'''


#Sample Input
#     Welcome to 30 Days of Code!

#Sample Output
#     Hello, World. 
#     Welcome to 30 Days of Code!

#Explanation
#On the first line, we print the string literal Hello, World.. On the second line, we print the contents of the input string variable which, 
# for this sample case, happens to be Welcome to 30 Days of Code!. If you do not print 
#the variable's contents to stdout, you will not pass the hidden test case



input_string = input() #Welcome to 30 Days of Code!

# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')
print(input_string)