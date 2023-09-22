# https://atcoder.jp/contests/abc143/tasks/abc143_b
N = int(input())
d_arr = list(map(int, input().split()))
ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        ans += d_arr[i] * d_arr[j]
print(ans)
