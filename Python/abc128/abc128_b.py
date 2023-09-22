# https://atcoder.jp/contests/abc128/tasks/abc128_b
N = int(input())
data = []
for i in range(N):
    c, p = input().split()
    p = int(p)
    data.append([c, p, i + 1])
sorted_data = sorted(data, key=lambda x: (x[0], -x[1]))
for d in sorted_data:
    print(d[2])
