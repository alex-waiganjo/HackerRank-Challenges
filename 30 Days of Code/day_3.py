#TASK
'''
Given an integer ,n ,Perform the following conditional actions:
   => If n is odd,Print 'Weird'
   => If n is even and in the inclusive of 2 to 5, Print 'Not Weird'
   => If n is even and in the inclusive of 6 to 20 ,Print  'Weird'
   => If n is even and greater than 20 ,Print 'Not Weird'
 '''


 
if __name__ == '__main__':
    N = int(input().strip())


#SOLUTIONS

#  Method 1        ------- Good Readable Code -----
if N%2 ==0:
    if N in range(2,5):
        print('Not Weird')
    if N==20 or N in range(6,20):
        print('Weird')
    if N>20:
        print('Not Weird')        
else:
     print('Weird')    


#  Method 2       ------ Poorly Structured Code -------
if N%2 == 1:
    print('Weird')
if N%2 == 0 and N in range(2,5):
    print('Not Weird')
if N%2 == 0 and N==20 or N in range(6,20):
    print('Weird')
if N%2 == 0 and N>20:
    print('Not Weird')   