# https://atcoder.jp/contests/jsc2021/tasks/jsc2021_a
from math import ceil
X, Y, Z = map(int, input().split())
ans = ceil(Y * Z / X)
print(ans - 1)
