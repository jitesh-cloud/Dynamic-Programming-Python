# canSum(ts,arr) function verifies the targetSum can be achieved from the numbers in array
# If targetSum is achieved it returns-True and if not then returns-False
# If targetSum is equal to 0 returns True ==> Coz we can definitely generate 0 sum by taking no numbers
# If targetSum is less than 0 returns False ==>
# To generate a proper output we required to check every possible element so here comes for loop
# In for loop, to check the elements of targetSum remainder is created ==> remainder = targetSum - num
# Now remainder is used as targetSum and again same array elements given to the function ==> we can use array numbers as many times as we want
# It will run the code until it gets True/False as a result
# canSum() function : before Memoization
# def canSum(ts, arr):
#     if ts == 0:
#         return True
#     if ts < 0:
#         return False
#     for num in arr:
#         remainder = ts - num
#         if canSum(remainder, arr) == True:
#             return True
#     return False

# canSum() function : after Memoization
def canSum(ts, arr, memo={}):
    if ts in memo:
        return memo[ts]
    if ts == 0:
        return True
    if ts < 0:
        return False
    for num in arr:
        remainder = ts - num
        if canSum(remainder, arr, memo) == True:
            return True
    memo[ts] = False
    return memo[ts]

# targetSum = 7 and array = [2,3]
print(canSum(7,[2,3])) # True ==> 7 can be achieved by 2+3+2
# targetSum = 7 and array = [2,4]
print(canSum(7,[2,4])) # False ==> not possible in any way
# targetSum = 300 and array = [7,14]
print(canSum(300,[7,14])) # Time required to solve this is more
# After memoization time is really less than every thing
