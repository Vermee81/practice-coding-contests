# https://atcoder.jp/contests/abc210/tasks/abc210_c
from collections import Counter
N, K = map(int, input().split())
c = list(map(int, input().split()))
firstK = c[:K]
collect = Counter(firstK)
color = len(collect)
first = c[0]
if N == K:
    print(color)
    exit()
for i in range(1, N - K + 1):
    last = c[i + K - 1]
    collect[last] += 1
    collect[first] -= 1
    if collect[first] == 0:
        del collect[first]
    col = len(collect)
    color = max(color, col)
    first = c[i]
print(color)
