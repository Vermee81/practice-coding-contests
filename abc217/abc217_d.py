# https://atcoder.jp/contests/abc217/tasks/abc217_d
from bisect import bisect_right
import array
L, Q = map(int, input().split())
arr = array.array('i', [0, L])
for _ in range(Q):
    c, x = map(int, input().split())
    y = bisect_right(arr, x)
    if c == 1:
        arr.insert(y, x)
        continue
    print(arr[y] - arr[y - 1])
