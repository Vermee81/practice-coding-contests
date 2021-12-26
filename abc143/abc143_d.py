# https://atcoder.jp/contests/abc143/tasks/abc143_d
from bisect import bisect_left

N = int(input())
l_arr = list(map(int, input().split()))
l_arr.sort()
ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        a = l_arr[i]
        b = l_arr[j]

        k = bisect_left(l_arr, a + b)
        print(i, j, k)
        ans += max(k - j - 1, 0)

print(ans)
