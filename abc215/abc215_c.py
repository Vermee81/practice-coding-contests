# https://atcoder.jp/contests/abc215/tasks/abc215_c
from itertools import permutations
S, K = input().split()
K = int(K)
S_arr = [s for s in S]
S_arr.sort()
patterns = permutations(S_arr, len(S_arr))
list_pat = list(set(patterns))
pat_str = []
for lp in list_pat:
    pat_str.append("".join(lp))
pat_str.sort()
print(pat_str[K - 1])
