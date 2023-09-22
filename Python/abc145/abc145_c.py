# https://atcoder.jp/contests/abc145/tasks/abc145_c
from itertools import permutations
from math import sqrt
N = int(input())
towns = []
for _ in range(N):
    x, y = [int(i) for i in input().split()]
    towns.append((x, y))
towns_distance = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        towns_distance[i][j] = sqrt((towns[i][0] - towns[j][0])**2 + (towns[i][1] - towns[j][1])**2)
patterns = list(permutations([i for i in range(N)]))
total = 0
for m in patterns:
    for i in range(N-1):
        total += towns_distance[m[i]][m[i+1]]
print(round(total/len(patterns), 10))
