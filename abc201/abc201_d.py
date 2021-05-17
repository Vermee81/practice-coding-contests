# https://atcoder.jp/contests/abc201/tasks/abc201_d
Y, X = map(int, input().split())
INF = 10**9 + 7
zahyo = [[-1 for _ in range(X)] for _ in range(Y)]
opt = [[-INF for _ in range(X)] for _ in range(Y)]
taka = 0
aoki = 0
for y in range(Y):
    row = input()
    for x, r in enumerate(row):
        if x == 0 and y == 0:
            continue
        if r == '+':
            zahyo[y][x] = 1

for y in range(Y - 1, -1, -1):
    for x in range(X - 1, -1, -1):
        if y == Y - 1 and x == X - 1:
            opt[y][x] = 0
            continue
        if y < Y - 1:
            opt[y][x] = max(opt[y][x], zahyo[y + 1][x] - opt[y + 1][x])
        if x < X - 1:
            opt[y][x] = max(opt[y][x], zahyo[y][x + 1] - opt[y][x + 1])

if opt[0][0] < 0:
    print('Aoki')
    exit()
if opt[0][0] > 0:
    print('Takahashi')
    exit()

print('Draw')
