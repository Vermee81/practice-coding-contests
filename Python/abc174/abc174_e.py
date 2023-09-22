# https://atcoder.jp/contests/abc174/tasks/abc174_e
from math import ceil
N, K = map(int, input().split())
a_arr = list(map(int, input().split()))

ok = max(a_arr)
ng = (min(a_arr) // (K + N))
ans = ok


def can_cut(x):
    cut_sum = 0
    for a in a_arr:
        cut_sum += ceil(a / x) - 1
    if cut_sum <= K:
        return True
    else:
        return False


while ok - ng > 1:
    mid = (ok + ng) // 2
    if can_cut(mid):
        ok = mid
        ans = mid
    else:
        ng = mid

print(ans)
