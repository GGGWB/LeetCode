import sys
def max_coin(n, arr):
    dp = [([0]*n) for i in range(n)]
    dp[0][0] = int(arr[0][0])
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + int(arr[i][0])
        dp[i][i] = dp[i-1][i-1] + int(arr[i][i])
    for i in range(n):
        for j in range(i):
            dp[i][j] = max(dp[i-1][j-1]+int(arr[i][j]), dp[i-1][j]+int(arr[i][j]))
    return max([dp[n-1][p] for p in range(n)])

n = int(input())
ll = []
for line in sys.stdin:
    a = line.split()
    ll.append(a)
x = max_coin(n, ll)
print(x)