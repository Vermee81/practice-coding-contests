# https://atcoder.jp/contests/abc180/tasks/abc180_b
from math import sqrt
N = int(input())
x_arr = list(map(int, input().split()))
man = 0
euc = 0
cheb = 0
for x in x_arr:
    cheb = max(cheb, abs(x))
    man += abs(x)
    euc += x**2
print(man)
print(round(sqrt(euc), 10))
print(cheb)
