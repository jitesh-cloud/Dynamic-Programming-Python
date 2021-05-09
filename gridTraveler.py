# Grid Traveller problem : Finding out Number of ways to reach destination (m,n)
# Grid is 2D with m*n dimensions
# Starting from top-left corner and ending on the botttom-right
# You have to move one step at a time i.e Either go down(m,n-1) or go right(m-1,n)
# gridTraveller() func before memoization :
# def gridTraveller(m,n):
#     if (m == 1 and n == 1):
#         return 1
#     if (m == 0 or n == 0):
#         return 0
#     return gridTraveller(m-1,n) + gridTraveller(m,n-1)

# gridTraveller() func after memoization :
def gridTraveller(m, n, memo = {}):
    key = "{0},{1}".format(m,n)
    # All the args in the memo
    if (key in memo): return memo[key]
    if (m == 1 and n == 1): return 1
    if (m == 0 or n == 0): return 0

    memo[key] = gridTraveller(m-1,n,memo) + gridTraveller(m,n-1,memo)
    return memo[key]

# It will print the result : No. of ways to reach (m,n)
# (m,n) = (1,1)/(4,6) : Smaller values required less time and can be returned w/o memoization technique
print(gridTraveller(1,1)) # (1,1) ==> 1
print(gridTraveller(4,6)) # (4,6) ==> 56
# (m,n) = (12,10)/(23,17) : Bigger values cannot be resolved w/o memoiztion of gridTraveller() func
print(gridTraveller(12,10)) # (12,10) ==> 167960
print(gridTraveller(23,17)) # (23,17) ==> 22239974430
