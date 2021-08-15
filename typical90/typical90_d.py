# https://atcoder.jp/contests/typical90/tasks/typical90_d
H, W = map(int, input().split())
graph = []
ans_graph = [[0 for _ in range(W)] for _ in range(H)]
for _ in range(H):
    w_list = list(map(int, input().split()))
    graph.append(w_list)

H_sum_list = []
for h in range(H):
    H_sum_list.append(sum(graph[h]))
W_sum_list = []
for w in range(W):
    add = 0
    for h in range(H):
        add += graph[h][w]
    W_sum_list.append(add)

for h in range(H):
    row_list = []
    for w in range(W):
        row_list.append(H_sum_list[h] + W_sum_list[w] - graph[h][w])
    ans_str = " ".join([str(s) for s in row_list])
    print(ans_str)
