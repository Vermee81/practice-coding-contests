# https://atcoder.jp/contests/abc203/tasks/abc203_d
N, K = map(int, input().split())
a_map = [list(map(int, input().split())) for _ in range(N)]
s_map = [[0 for _ in range(N + 3)] for _ in range(N + 3)]

shikii = (K**2 // 2) + 1


def has_lower(x: int) -> bool:
    for i in range(N):
        for j in range(N):
            s_map[i + 1][j + 1] = s_map[i][j + 1] + s_map[i + 1][j] - s_map[i][j]
            if a_map[i][j] > x:
                s_map[i + 1][j + 1] += 1
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            if (s_map[i + K][j + K] - s_map[i + K][j] - s_map[i][j + K] + s_map[i][j]) < shikii:
                return True
    return False


ng = -1
ok = 10**9
while ok - ng > 1:
    mid = (ok + ng) // 2
    if has_lower(mid):
        ok = mid
    else:
        ng = mid

print(ok)
