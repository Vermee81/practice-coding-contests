# https://atcoder.jp/contests/abc156/tasks/abc156_c
N = int(input())
x_arr = sorted(list(map(int, input().split())))
ans = 10**9 + 7
for p in range(x_arr[0], x_arr[-1] + 1):
    total = 0
    for x in x_arr:
        total += (x - p) ** 2
    ans = min(ans, total)
print(ans)
