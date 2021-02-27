# https://atcoder.jp/contests/abc193/tasks/abc193_c
from math import log2
from math import floor, ceil
from math import sqrt
N = int(input())
max_b = floor(log2(N))
max_a = ceil(sqrt(N))
ok_set = set()
for b in range(2, max_b + 1):
    for a in range(2, max_a + 1):
        if a ** b <= N:
            ok_set.add(a**b)
        else:
            break
count = len(ok_set)
print(N - count)
