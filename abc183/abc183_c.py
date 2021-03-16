# https://atcoder.jp/contests/abc183/tasks/abc183_c
from itertools import permutations

N, K = map(int, input().split())
t_map = [list(map(int, input().split())) for _ in range(N)]

# 最初と最後の1は含んでいない全ルートを列挙する
routes = list(permutations(range(2, N + 1), N - 1))

ok_routes = 0
for route in routes:
    # ルートの最初と最後に1を追加する
    r = [1]
    r.extend(list(route))
    r.extend([1])

    total = 0
    # ルートの合計時間を計算する
    for i in range(N):
        if total > K:
            break
        total += t_map[r[i] - 1][r[i + 1] - 1]
    # Kと一致してたらOK
    if total == K:
        ok_routes += 1
print(ok_routes)
