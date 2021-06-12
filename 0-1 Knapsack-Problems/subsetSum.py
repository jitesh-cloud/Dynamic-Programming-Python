# Knapsack Pattern Problems
# Author: Jitesh Bagul
"""
Subset-Sum Problem :
To detect the knapsack problem you need to check for two things -
1. Given a or two arrays in the problem statements - wt[]/val[]
2. Capacity of a knapsack is given (W)
We need to find the optimal solution by taking values or weights in the arrays given.
"""
# Subset Sum problem here clarifies that the numbers given in the array could reach the sum given or not.
# Basically it returns the True/False (Boolean Values) or Yes/No directly.

# Here we are defining the func()-subsetSum(array,givenSum,lengthOfArray)
def subsetSum(arr,sum,no):

    # Base Condition of the program
    # If len(array) is zero returns False
    if no == 0:
        return False
    # If sum is zero then we cam achieve the sum=0 by taking null set '{}' so returns True
    elif sum == 0:
        return True

    # Actual Recursion/Choice Diagram
    # The choices are decided with some mental calculations/predictions
    # If sum is less than array element then we cannot accept such values then we'll omit that element w/o changing sum and goes for next
    elif sum < arr[no-1]:
        return subsetSum(arr,sum,no-1)

    # If sum is greater than or equal to the element in an array then here are two choices to consider or omit
    # And as we are asked for the Boolean Values in return we will choose for most significant
    # So we used or statement in the condition used below
    # If we accept the value the sum will decrease by the element value used and length of array will also decrease by 1
    # If we omit the element then the condition lies exactly same as the previous condition directly omits the element but length of array is also decrease by 1 w/o changing sum
    elif sum >= arr[no-1]:
        return (subsetSum(arr,sum-arr[no-1],no-1) | (subsetSum(arr,sum,no-1)))

arr = list(map(int,input("Enter the array elements: ").strip().split()))
sum = int(input("Enter SUM value to check optimal solution: "))

print(subsetSum(arr,sum,len(arr)))
