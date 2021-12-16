# https://atcoder.jp/contests/abc113/tasks/abc113_c
from math import log10
N, M = map(int, input().split())
towns = []
for i in range(M):
    p, m = map(int, input().split())
    towns.append([p, m, i])


def add_zeros(num: int) -> str:
    keta = int(log10(num)) + 1
    prefix_zero = '0' * (6 - keta)
    return prefix_zero + str(num)


towns = sorted(towns, key=lambda x: (x[0], x[1]))
sorted_towns = [[0, 0] for _ in range(M)]
prev_pref = towns[0][0]
counter = 1

for i, t in enumerate(towns):
    prefecture, month, index = t[0], t[1], t[2]

    pref_str = add_zeros(prefecture)

    if i != 0:
        if prev_pref == prefecture:
            counter += 1
        else:
            prev_pref = prefecture
            counter = 1

    counter_str = add_zeros(counter)
    sorted_towns[index][1] = pref_str + counter_str

for s in sorted_towns:
    print(s[1])

