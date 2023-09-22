# https://atcoder.jp/contests/abc181/tasks/abc181_c
from itertools import combinations
N = int(input())
zahyo = []
for _ in range(N):
    zahyo.append(list(map(int, input().split())))

for pat in combinations(zahyo, 3):
    x1_x2 = pat[0][0] - pat[1][0]
    y1_y2 = pat[0][1] - pat[1][1]
    left = x1_x2 * (pat[2][1] - pat[0][1])
    right = y1_y2 * (pat[2][0] - pat[0][0])
    if left == right:
        print('Yes')
        exit()
print('No')