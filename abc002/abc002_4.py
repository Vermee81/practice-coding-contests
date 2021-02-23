# https://atcoder.jp/contests/abc002/tasks/abc002_4
from itertools import combinations
N, M = list(map(int, input().split()))
friends = [[0 for _ in range(N)] for _ in range(N)]
max_count = 0
if M == 0:
    print(1)
    exit()
for _ in range(M):
    x, y = list(map(int, input().split()))
    friends[x-1][y-1] = 1
    friends[y-1][x-1] = 1
for bit in range(1 << N):
    fr_list = []
    for i in range(N):
        if bit & (1 << i):
            fr_list.append(i)
    hantei = True
    for com in list(combinations(fr_list, 2)):
        if friends[com[0]][com[1]] == 0 or friends[com[1]][com[0]] == 0:
            hantei = False
            break
    if hantei:
        max_count = max(max_count, len(fr_list))
print(max_count)
