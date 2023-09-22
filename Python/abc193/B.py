# https://atcoder.jp/contests/abc193/tasks/abc193_b
from math import ceil
N = int(input())
min_val = 10**9

for _ in range(N):
  a, p, x = list(map(int, input().split()))
  heru = ceil((a - 0.5) / 1.0)
  remain = x - heru
  if remain > 1:
    min_val = min(min_val, p)

print(min_val)
