# https://atcoder.jp/contests/typical90/tasks/typical90_c
from collections import deque
N = int(input())
graph = [[] for _ in range(N)]


def bfs(x: int):
    dist = [-1] * N
    dist[x] = 0
    q = deque([x])
    while len(q):
        now = q.popleft()
        for next in graph[now]:
            if dist[next] != -1:
                continue
            dist[next] = dist[now] + 1
            q.append(next)
    return dist


for _ in range(N - 1):
    f, t = map(int, input().split())
    graph[f - 1].append(t - 1)
    graph[t - 1].append(f - 1)


dist = bfs(0)
farthest_node = dist.index(max(dist))

dist = bfs(farthest_node)
print(max(dist) + 1)

