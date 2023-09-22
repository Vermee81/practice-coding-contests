# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=ja
N, W = map(int, input().split())
value_arr = []
weight_arr = []
for _ in range(N):
    v, w = map(int, input().split())
    value_arr.append(v)
    weight_arr.append(w)

dp = [[-1 for _ in range(W + 1)] for _ in range(N + 1)]

# i: i番目の品物、j: トータルの重さ
# dp[i][j]: i番目までのものから、重さがjを超えないように選んだ時の価値の最大値
# dp[i + 1][j] = dp[i][j]
# dp[i + 1][j] = dp[i][j - weight_arr[i]] + value_arr[i]

for j in range(W + 1):
    dp[0][j] = 0

for i in range(N):
    for j in range(W + 1):
        if j >= weight_arr[i]:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - weight_arr[i]] + value_arr[i])
            continue
        dp[i + 1][j] = dp[i][j]

print(dp[N][W])
