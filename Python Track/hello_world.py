#Task 1
# You can just as easily store a string as a variable and then print it to stdout:
if __name__ == '__main__':
    print("Hello, World!")


# Task 2
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last

# Sample Input
# Ross
# Taylor

# Output
# Hello Ross Taylor! You just delved into python.

def print_full_name(first, last):
    # Write your code here
    print(f'Hello {first} {last}! You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)    


# Task  3
# You are given a string.Split the string on a "" space(delimeter) and join using a -hypen

#Function Description
# split_and_join has the following parameters:
# string line: a string of space-separated words

#SAMPLE INPUT
# this is a string

# SAMPLE OUTPUT
# this-is-a-string


line= input()


def split_and_join(line):
    l = line.split(' ')
    b = "-".join(l)
    print(b)

split_and_join(line)




