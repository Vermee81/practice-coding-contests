# https://atcoder.jp/contests/abc148/tasks/abc148_c
from math import gcd
A, B = map(int, input().split())
print(int(A * B / gcd(A, B)))
