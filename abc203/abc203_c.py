# https://atcoder.jp/contests/abc203/tasks/abc203_c
N, K = map(int, input().split())
b_arr = [list(map(int, input().split())) for _ in range(N)]

b_arr = sorted(b_arr)
until = K

for b in b_arr:
    if until >= b[0]:
        until += b[1]

print(until)
