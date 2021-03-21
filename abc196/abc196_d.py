# https://atcoder.jp/contests/abc196/tasks/abc196_d
H, W, A, B = map(int, input().split())

# 畳で埋まってるかどうかを記録
used = [[False for _ in range(16)] for _ in range(16)]


def dfs(i: int, j: int, a: int, b: int):
    # どちらかの畳を使い切る
    if a < 0 or b < 0:
        return 0
    # 一番右端に来た時に、左端に戻しつつ下を見る
    if j == W:
        j = 0
        i += 1
    # 一番下に到達したら終了
    if i == H:
        return 1
    # 畳で埋まってたら右隣を探索
    if used[i][j]:
        return dfs(i, j + 1, a, b)
    res = 0
    used[i][j] = True
    # 半畳を使った場合
    res += dfs(i, j + 1, a, b - 1)
    # 横にAを置く場合
    # j + 1 がWに収まってて、i, j+1が埋まってない
    if not used[i][j + 1] and j + 1 < W:
        used[i][j + 1] = True
        res += dfs(i, j + 1, a - 1, b)
        # 1つ上の深さに戻るので未使用にする
        used[i][j + 1] = False
    # 縦にAを置く場合
    # i + 1がHに収まってて、i + 1, j が埋まってない
    if not used[i + 1][j] and i + 1 < H:
        used[i + 1][j] = True
        res += dfs(i, j + 1, a - 1, b)
        # 1つ上の深さに戻るので未使用にする
        used[i + 1][j] = False
    used[i][j] = False
    return res


# 左上から探索開始
print(dfs(0, 0, A, B))
