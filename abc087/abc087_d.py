# https://atcoder.jp/contests/abc087/tasks/arc090_b
from collections import deque
N, M = map(int, input().split())
link = [[] for _ in range(N)]
for _ in range(M):
    l, r, d = map(int, input().split())
    link[l - 1].append([r - 1, d])
    link[r - 1].append([l - 1, -d])


def bfs(s):
    que = deque([s])
    while que:
        x = que.popleft()
        for nx, dist in link[x]:
            np = visited[x] + dist
            if visited[nx] != INF and visited[nx] != np:
                print('No')
                exit()

            if visited[nx] != INF:
                continue

            visited[nx] = np
            que.append(nx)


INF = -10**10
visited = [INF] * N
for i in range(N):
    if visited[i] != INF:
        continue
    visited[i] = 0
    bfs(i)

print('Yes')
