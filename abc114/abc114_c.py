# https://atcoder.jp/contests/abc114/tasks/abc114_c
from math import log10
from itertools import product
N = int(input())
max_keta = int(log10(N)) + 1

ans = 0

for keta in range(1, max_keta + 1):
    search_list = product(range(3), repeat=keta)
    for sl in search_list:
        # 3進数で 2 -> 7, 1 -> 5, 0 -> 3 とする
        # 7か5か3が1回以上含まれていなかったら次のパターンへ行く
        if not (2 in sl and 1 in sl and 0 in sl):
            continue
        # 210 だったら 753 に変換する
        # len = 3 のとき index 0 だったら 10^2 をかけて足す
        # len - index - 1 で 3 - 0 - 1 = 2, 3 - 1 - 1 = 1, 3 - 2 - 1 = 0
        number = 0
        TRANS = [3, 5, 7]
        for j, n in enumerate(sl):
            number += 10**(len(sl) - j - 1) * TRANS[n]
        if number <= N:
            ans += 1

print(ans)
