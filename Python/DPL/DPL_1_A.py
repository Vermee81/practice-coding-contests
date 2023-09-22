# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=ja
n, m = map(int, input().split())
c_arr = list(map(int, input().split()))
c_arr.sort()
max_maisu = n // c_arr[0] + 1
dp = [max_maisu for _ in range(n + 1)]
for c in c_arr:
    if c <= n:
        dp[c] = 1

# dp[i] i円支払う時の最小枚数
# c円玉を使うとき
# dp[i] = dp[i - c] + 1
for i in range(1, n + 1):
    # iがコインの最小値より低ければ、パス
    if i < c_arr[0]:
        continue
    for c in c_arr:
        # i - c が0未満だと、1つ前のステップがマイナスになってしまう
        if i - c >= 0:
            dp[i] = min(dp[i], dp[i - c] + 1)
print(dp[n])
