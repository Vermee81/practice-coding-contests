# https://atcoder.jp/contests/abc131/tasks/abc131_d
N = int(input())
tasks = []
for _ in range(N):
    a, b = map(int, input().split())
    tasks.append([a, b])
tasks = sorted(tasks, key=lambda x: x[1])
time = 0
for t in tasks:
    time += t[0]
    if time > t[1]:
        print('No')
        exit()
print('Yes')
