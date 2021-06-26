# https://atcoder.jp/contests/abc207/tasks/abc207_b
from math import ceil
A, B, C, D = map(int, input().split())
if C*D - B <= 0:
    print(-1)
    exit()
kaisu = A / (C*D - B)
ans = ceil(kaisu)
print(ans)
