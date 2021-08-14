# https://atcoder.jp/contests/abc171/tasks/abc171_d
from collections import Counter
N = int(input())
a_arr = list(map(int, input().split()))
memo = Counter(a_arr)
ans = sum(a_arr)
Q = int(input())
for _ in range(Q):
    b, c = map(int, input().split())
    diff = c - b
    if memo[b]:
        tmp = memo[b]
        memo[b] = 0
        memo[c] += tmp
        ans += diff * tmp
    print(ans)

