# https://atcoder.jp/contests/abc219/tasks/abc219_d
N = int(input())
X, Y = map(int, input().split())
ab_arr = []
for _ in range(N):
    a, b = map(int, input().split())
    ab_arr.append([a, b])

#x_arr = [10**9] * 310
#y_arr = [x_arr] * 310
#dp = [y_arr] * (N + 1)
dp = [[[(10**9) for _ in range(Y + 1)] for _ in range(X + 1)] for _ in range(N + 1)]

dp[0][0][0] = 0

for i in range(N):
    for j in range(X + 1):
        for k in range(Y + 1):
            jj = min(X, j + ab_arr[i][0])
            kk = min(Y, k + ab_arr[i][1])
            dp[i + 1][j][k] = min(dp[i][j][k], dp[i + 1][j][k])
            dp[i + 1][jj][kk] = min(dp[i][j][k] + 1, dp[i + 1][jj][kk])

ans = dp[N][X][Y] if dp[N][X][Y] != (10**9) else -1
print(ans)


