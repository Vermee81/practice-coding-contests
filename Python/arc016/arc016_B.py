# https://atcoder.jp/contests/arc016/tasks/arc016_2
N = int(input())
count = 0
fumen = []
for _ in range(N):
    fumen.append([s for s in input()])

for c in range(9):
    uncount_flag = False
    for r in range(N):
        if fumen[r][c] == 'x':
            count += 1
            uncount_flag = False
            continue
        if fumen[r][c] == 'o' and not uncount_flag:
            count += 1
            uncount_flag = True
            continue
        if fumen[r][c] == 'o' and uncount_flag:
            continue
        uncount_flag = False

print(count)
