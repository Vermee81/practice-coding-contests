# https://atcoder.jp/contests/abc211/tasks/abc211_d
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

que = [0]
dist = [None] * N
cnt = [0] * N
dist[0] = 0
cnt[0] = 1

for v in que:
    for vv in G[v]:
        if dist[vv] is None:
            dist[vv] = dist[v] + 1
            que.append(vv)
            cnt[vv] = cnt[v]
            continue
        if dist[vv] == dist[v] + 1:
            cnt[vv] += cnt[v]
            cnt[vv] %= 10**9 + 7
            continue

print(cnt[N - 1])
