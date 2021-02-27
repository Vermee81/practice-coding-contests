# https://atcoder.jp/contests/abc150/tasks/abc150_c
from itertools import permutations
N = int(input())
lst = [i for i in range(1, N + 1)]
P = tuple(int(i) for i in input().split())
Q = tuple(int(i) for i in input().split())
all_lst = list(permutations(lst))
p_idx = 0
q_idx = 0
for i, e in enumerate(all_lst):
    if e == P:
        p_idx = i
    if e == Q:
        q_idx = i
print(abs(p_idx - q_idx))
