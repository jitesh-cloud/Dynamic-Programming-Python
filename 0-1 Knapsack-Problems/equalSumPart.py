# Knapsack Pattern Problems:
"""
Equal-Sum-Partition Problem :
This problem asks is it possible to achieve the equal sum for the two subsets of the given array.
Basically it returns the True/False (Boolean Values) or Yes/No directly.
"""
# We will use the subsetSum function from previous problem in here
# Here we are defining the func()-subsetSum(array,givenSum,lengthOfArray)
def subsetSum(arr,sum,n):
    if n == 0:
        return False

    elif sum == 0:
        return True

    elif sum < arr[n-1]:
        return subsetSum(arr,sum,n-1)

    elif sum >= arr[n-1]:
        return (subsetSum(arr,sum-arr[n-1],n-1) | (subsetSum(arr,sum,n-1)))

# Here we are defining the actual func()- equalSumPartition(array, sum = 0)
def equalSumP(arr,sum=0):

    # Base Condition :
    # We need to carry out sum of the array first
    for i in arr:
        sum = sum + i

    # If sum is odd then it will definitely not convert the array in two equal subsets so returns False
    if sum % 2 != 0:
        return False

    # If sum is even then there  is possibility of getting two subarrays having equal sum
    # So we are checking for even or not
    # We will be passing the sum/2 value to the subsetSum()
    # If we want the two subarrays then sum must be equal
    # By passing sum/2 we gonna confirm the first subarray using subsetSum()
    # So Indirectly we are checking for both the subarrays because if one is generated and checked then other will definitely form
    elif sum % 2 == 0:
        return subsetSum(arr, sum/2, len(arr))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print(equalSumP(arr,0))
