import numpy as np

maxN = 20
maxSum = 50
minSum = 50
base = 50

dp = np.zeros((maxN, maxSum + minSum))
v = np.zeros((maxN, maxSum + minSum))

def findCnt(arr, i, rq_sum, n):

    # Base Case
    if (i == n):
        if (rq_sum == 0):
            return 1
        else:
            return 0

    # If state has been solved before return the value of state
    if  (v[i][rq_sum + base]):
        return dp[i][rq_sum + base]

    v[i][rq_sum + base] = 1

    dp[i][rq_sum + base] = findCnt(arr,i+1,rq_sum,n) + findCnt(arr,i+1,rq_sum-arr[i],n)

    return dp[i][rq_sum + base]

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    x = int(input())

    print(findCnt(arr, 0, x, len(arr)))
