# https://atcoder.jp/contests/abc197/tasks/abc197_b
H, W, X, Y = map(int, input().split())
graph = [[s for s in input()] for _ in range(H)]

s_r = X - 1
s_c = Y - 1

# 最初の位置は重複して数えるので3引いておく
count = -3

# 下へ探索
for i in range(s_r, H):
    if graph[i][s_c] != '.':
        break
    count += 1
# 上へ探索
for i in range(s_r, -1, -1):
    if graph[i][s_c] != '.':
        break
    count += 1
# 右へ探索
for i in range(s_c, W):
    if graph[s_r][i] != '.':
        break
    count += 1
# 左へ探索
for i in range(s_c, -1, -1):
    if graph[s_r][i] != '.':
        break
    count += 1

print(count)
