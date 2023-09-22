# https://atcoder.jp/contests/abc186/tasks/abc186_d
N = int(input())
a_arr = list(map(int, input().split()))
ruiseki = [0] * N
a_arr.sort()

for i, a in enumerate(a_arr):
    if i == 0:
        ruiseki[i] = a_arr[0]
        continue
    ruiseki[i] = ruiseki[i - 1] + a

ans = 0

for j in range(1, N):
    ans += a_arr[j] * j - ruiseki[j - 1]

print(ans)
