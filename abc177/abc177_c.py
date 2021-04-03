# https://atcoder.jp/contests/abc177/tasks/abc177_c
N = int(input())
a_arr = list(map(int, input().split()))
MOD = 10**9 + 7
add_cum = a_arr[0] % MOD
ans = 0
for i in range(1, N):
    ans += (a_arr[i] % MOD) * add_cum % MOD
    add_cum += a_arr[i] % MOD
print(ans % MOD)
