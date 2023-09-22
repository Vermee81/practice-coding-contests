# https://atcoder.jp/contests/abc206/tasks/abc206_c
from collections import Counter
N = int(input())
a_arr = list(map(int, input().split()))
rui_dict = Counter(a_arr)
minus = 0
for v in rui_dict.values():
    minus += (v * (v - 1)) // 2
ans = N * (N - 1) // 2 - minus
print(ans)
