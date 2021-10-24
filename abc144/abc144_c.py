# https://atcoder.jp/contests/abc144/tasks/abc144_c
N = int(input())
yakusu = []
i = 1
while i*i <= N:
    if N % i == 0:
        yakusu.append([i, N // i])
    i += 1

val = 10 ** 12
for y in yakusu:
    dist = y[0] - 1 + y[1] - 1
    if dist < val:
        val = dist
print(val)
