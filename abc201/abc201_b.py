# https://atcoder.jp/contests/abc201/tasks/abc201_b
N = int(input())
mountains = []
for _ in range(N):
    s, t = input().split()
    t = int(t)
    mountains.append([s, t])

mount = sorted(mountains, key=lambda x: x[1], reverse=True)
print(mount[1][0])
