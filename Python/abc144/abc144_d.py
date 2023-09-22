# https://atcoder.jp/contests/abc144/tasks/abc144_d
from math import atan, degrees
a, b, x = map(float, input().split())
half = a * a * b / 2
if x > half:
    keisan = (2 * a**2 * b - 2 * x) / (a ** 3)
else:
    keisan = (a * b**2) / (2 * x)

ans = degrees(atan(keisan))
print(ans)
