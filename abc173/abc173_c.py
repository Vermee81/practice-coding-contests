# https://atcoder.jp/contests/abc173/tasks/abc173_c
import copy
H, W, K = map(int, input().split())
masu = [[i for i in input()] for _ in range(H)]
ans = 0


def paint_row(t_masu: list, row_idx: int) -> list:
    for i, _ in enumerate(t_masu[row_idx]):
        t_masu[row_idx][i] = -1
    return t_masu


def paint_column(t_masu: list, col_idx: int) -> list:
    for i in range(H):
        t_masu[i][col_idx] = -1
    return t_masu


def count_red(t_masu: list) -> int:
    counter = 0
    for r in t_masu:
        for c in r:
            if c == '#':
                counter += 1
    return counter


for bit_h in range(2**H):
    for bit_w in range(2**W):
        temp = copy.deepcopy(masu)
        for i in range(H):
            if bit_h & (1 << i):
                temp = paint_row(temp, i - 1)
        for j in range(W):
            if bit_w & (1 << j):
                temp = paint_column(temp, j - 1)
        if count_red(temp) == K:
            ans += 1

print(ans)
