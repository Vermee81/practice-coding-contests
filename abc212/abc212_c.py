# https://atcoder.jp/contests/abc212/tasks/abc212_c
from bisect import bisect_left
N, M = map(int, input().split())
a_arr = list(map(int, input().split()))
a_arr.sort()
b_arr = list(map(int, input().split()))
b_arr.sort()
if a_arr[N - 1] < b_arr[0]:
    print(abs(a_arr[N - 1] - b_arr[0]))
    exit()
if b_arr[N - 1] < a_arr[0]:
    print(abs(b_arr[M - 1] - a_arr[0]))
    exit()

ans = 10**10
start_j = 0
for i in range(N):
    start_j = bisect_left(a_arr, a_arr[i], )
    before_diff = 10**10
    for j in range(start_j, M):
        diff = abs(a_arr[i] - b_arr[j])
        if before_diff < diff:
            start_j = j
            break
        ans = min(ans, diff)

print(ans)
