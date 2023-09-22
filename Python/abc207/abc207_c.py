# https://atcoder.jp/contests/abc207/tasks/abc207_c
from itertools import combinations
N = int(input())
r_list = []
for _ in range(N):
    t, l, r = map(int, input().split())
    r_list.append([t, l, r])


def get_range(r):
    if r[0] == 1:
        return [r[1], r[2]]
    if r[0] == 2:
        return [r[1], r[2] - 0.1]
    if r[0] == 3:
        return [r[1] + 0.1, r[2]]
    return [r[1] + 0.1, r[2] - 0.1]


def hikaku(r1, r2) -> bool:
    r1_range = get_range(r1)
    r2_range = get_range(r2)
    if r1_range[1] >= r2_range[0] and r1_range[0] < r2_range[1]:
        return True
    if r2_range[1] >= r1_range[0] and r2_range[0] < r1_range[1]:
        return True
    return False


c_list = combinations(range(N), 2)
ans = 0
for c in c_list:
    if hikaku(r_list[c[0]], r_list[c[1]]):
        ans += 1
print(ans)
