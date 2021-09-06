# https://atcoder.jp/contests/abc157/tasks/abc157_b
a_graph = []
a_check = [[False for _ in range(3)] for _ in range(3)]
for _ in range(3):
    row_list = list(list(map(int, input().split())))
    a_graph.append(row_list)
N = int(input())
for _ in range(N):
    num = int(input())
    for r, row in enumerate(a_graph):
        for c, col in enumerate(row):
            if num == col:
                a_check[r][c] = True

for row in a_check:
    if not False in row:
        print('Yes')
        exit()

for c in range(3):
    if a_check[0][c] and a_check[1][c] and a_check[2][c]:
        print('Yes')
        exit()

if a_check[0][0] and a_check[1][1] and a_check[2][2]:
    print('Yes')
    exit()
if a_check[0][2] and a_check[1][1] and a_check[2][0]:
    print('Yes')
    exit()

print('No')
