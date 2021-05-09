"""
    m = target sum
    n = length of array

    Brute Force
    time: O(n^m * m)
    space: O(m)

    def howSum(target, arr):
    if target == 0:
        return []
    if target < 0:
        return None
    for num in arr:
        remainder = target - num
        result = howSum(remainder, arr)
        if result is not None:
            result.append(num)
            return result
    return None
"""





"""
    m = target sum
    n = length of array

    Memoize Version
    time: O(n*m*m) or O(n * m^2)
    space: O(m*m) or O(m^2)
"""

def howSum(ts, arr, memo=None):
    if memo is None:
        memo = {}
    if ts in memo:
        return memo[ts]
    if ts == 0:
        return []
    if ts < 0:
        return None
    for num in arr:
        rmd = ts - num
        rmRes = howSum(rmd, arr, memo)
        if rmRes is not None:
            rmRes.append(num)
            memo[ts] = rmRes
            return memo[ts]
    memo[ts] = None
    return None

testcases = [(7,[2,3]), (7,[5,3,4,7]), (7,[2,4]), (8,[2,3,5]), (300,[7,14])]

for test in testcases:
    targetSum, numbers = test
    print(f"canSum({targetSum},{numbers}) = {howSum(targetSum,numbers)}")
