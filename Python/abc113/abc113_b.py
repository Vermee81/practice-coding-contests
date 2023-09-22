# https://atcoder.jp/contests/abc113/tasks/abc113_b
N = int(input())
T, A = map(int, input().split())
h_arr = list(map(int, input().split()))
min_temp_diff = 10**9
ans = 5000
for i, h in enumerate(h_arr):
    temp = T - h * 0.006
    temp_diff = abs(temp - A)
    if min_temp_diff > temp_diff:
        ans = i + 1
        min_temp_diff = temp_diff

print(ans)
