# https://atcoder.jp/contests/typical90/tasks/typical90_h
N = int(input())
S = input()
MOD = 10 ** 9 + 7
T = 'atcoder'
dp = [[0 for _ in range(len(T) + 1)] for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][0] = 1
# dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
# dp[i][j] = dp[i - 1][j]
for j in range(1, len(T) + 1):
    for i in range(1, N + 1):
        if S[i - 1] == T[j - 1]:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][len(T)])

