# https://atcoder.jp/contests/abc064/tasks/abc064_c
N = int(input())
a_arr = list(map(int, input().split()))
color_set = set()
free_num = 0

for a in a_arr:
    if a >= 3200:
        free_num = free_num + 1
        continue
    color_set.add(a // 400)

if len(color_set) > 0:
    print(len(color_set), len(color_set) + free_num)
else:
    print(1, free_num)
