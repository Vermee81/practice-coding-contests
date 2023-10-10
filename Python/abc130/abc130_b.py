# https://atcoder.jp/contests/abc130/tasks/abc130_b
N, X = map(int, input().split())
l_list = list(map(int, input().split()))
d = 0
jump = 1
for i in range(2, N + 2):
    d += l_list[i - 2]
    if d <= X:
        jump += 1
print(jump)

