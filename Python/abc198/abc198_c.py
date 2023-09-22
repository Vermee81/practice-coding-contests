# https://atcoder.jp/contests/abc198/tasks/abc198_c
from math import sqrt, ceil
R, X, Y = map(int, input().split())
kyori = sqrt(X ** 2 + Y ** 2)
if kyori < R:
    print(2)
    exit()
ans = ceil(kyori / R)
print(ans)
