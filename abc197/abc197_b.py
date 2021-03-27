# https://atcoder.jp/contests/abc197/tasks/abc197_b
H, W, X, Y = map(int, input().split())
graph = [[s for s in input()] for _ in range(H)]

s_x = X - 1
s_y = Y - 1

count = 1

p_r = s_x - 1
p_c = s_y

# search up
while p_r >= 0 and graph[p_r][p_c] == '.':
    count += 1
    p_r -= 1

p_r = s_x + 1
p_c = s_y

# search down
while p_r < H and graph[p_r][p_c] == '.':
    count += 1
    p_r += 1

p_r = s_x
p_c = s_y - 1

# search left
while p_c >= 0 and graph[p_r][p_c] == '.':
    count += 1
    p_c -= 1

p_r = s_x
p_c = s_y + 1

# search right
while p_c < W and graph[p_r][p_c] == '.':
    count += 1
    p_c += 1

print(count)
