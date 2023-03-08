#TASK
'''
  Given a number n, for each integer i in the range from 1 to ninclusive,print one 
  value per line as follows
      => if i is a multiple of both 3 and 5, print 'FizzBuzz'
      => if i is a multiple of 3 (but not 5), print 'Fizz'
      => if i ia a multiple of 5(but not 3),print 'Buzz'
      => if i is not a multiple of 3 or 5, print the value i


      #SAMPLE INPUT
      n = 15

      #SAMPLE OUTPUT
      1     
      2
      Fizz
      4
      Buzz
      Fizz
      7
      8
      Fizz
      Buzz
      11
      Fizz
      13
      14
      FizzBuzz
'''

# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.

#SOLUTION
def fizzBuzz(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0:
            print('Fizz')  
        elif i%5==0:
            print('Buzz')
        else:
            print(i)       
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
