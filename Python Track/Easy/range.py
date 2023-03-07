#TASK
'''
Print the list of integers from 1 through n  as a string, without spaces.


              Input = 5
              Output = 12345
'''

#SOLUTION
n = int(input())
t = range(1,n+1)  
for p in t:
      print(p,end='') 

