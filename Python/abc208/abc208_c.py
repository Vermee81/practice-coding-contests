# https://atcoder.jp/contests/abc208/tasks/abc208_c
N, K = map(int, input().split())
a_arr = list(map(int, input().split()))
amap_arr = []
for i, a in enumerate(a_arr):
    amap_arr.append([i, a])
amap_arr = sorted(amap_arr, key=lambda x: x[1])
at_least = K // N
amari = K % N
for i in range(N):
    if i <= amari - 1:
        amap_arr[i][1] = at_least + 1
        continue
    amap_arr[i][1] = at_least
amap_arr = sorted(amap_arr, key=lambda x: x[0])
for i in range(N):
    print(amap_arr[i][1])

