# Fibonacci Series basically starts from 1 : It gives out next value to be the lastval+currentval
# 1,1,2,3,5,8,13,21,34,......... this is fibonacci series
# First two vals are always be 1, so in the fibo(n) function for n=1 or n=2 returns 1 always
# Other values will be counted on the basis of value of n depending to be more than 2 returns nextval = fibo(n-1)+fibo(n-2)
# Here func is making a tree to carry out operation
# fibo func before memoization:
# def fibo(n):
#     if n<=2:
#         return 1
#     return fibo(n-1)+fibo(n-2)

# Where code takes more time than it's required there comes a concept of Dynamic programming
# Memoization is the technique which simplifies the code by storing data and cuts out the repetition
# fibo func after memoization:
def fibo(n, memo = {}):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    memo[n] = fibo(n-1, memo)+fibo(n-2, memo)
    return memo[n]

# It will print the result : The fibonacci number at posN 'n'
# As n=6 is not so big, it can give result w/o using memoization technique
print(fibo(6)) # n=6 ==> 8
# As n=50 is much bigger than expected, it will definately take time due to much more tree branches will be checked by the Function
# Uses Memoization technique to reduce repetition
print(fibo(50)) # n=50 ==> 12586269025
