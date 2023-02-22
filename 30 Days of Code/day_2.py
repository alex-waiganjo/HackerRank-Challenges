'''
Given the meal price (base cost of a meal),
tip percent (the percentage of the meal price being added as tip), 
and tax percent (the percentage of the meal price being added as tax) for a meal, 
find and print the meal's total cost. 
Round the result to the nearest integer.
'''
#Example
# meal_cost = 12.0
# tip_percent=20
# tax_percent=8

#Output
# end_result = 15


#Calculations
# tip = 12/100*20  == 2.4
# tax = 8/100*12   == .96
# total cost = meal_cost + tip + tax = 15.36
# end_result = int(total_cost) //Round off





# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
     result1 = meal_cost/100*tip_percent
     result2 = tax_percent /100*meal_cost
     end_result = meal_cost+result1+result2
     print(round(end_result))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
