# https://atcoder.jp/contests/abc211/tasks/abc211_c
S = input()
C = 'chokudai'
M = len(S)
N = len(C)
INF = 10 ** 9 + 7
# Sのうちi文字までで作れるchokudaiのうちのj文字の個数
# dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
# dp[i][j] = dp[i][j - 1]
dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

for i in range(M + 1):
    dp[i][0] = 1

for i in range(M):
    for j in range(N):
        if S[i] == C[j]:
            dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i][j]) % INF
        else:
            dp[i + 1][j + 1] = dp[i][j + 1]

print(dp[M][8])

