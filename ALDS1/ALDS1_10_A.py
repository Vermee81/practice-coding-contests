# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A&lang=ja
N = int(input())

dp = [0 for _ in range(45)]
dp[0] = 1
dp[1] = 1

# dp[n] = db[n-1] + dp[n-2]
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N])
