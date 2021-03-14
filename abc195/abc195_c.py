# https://atcoder.jp/contests/abc195/tasks/abc195_c
from math import log10
N = int(input())

keta_mat = [0 for _ in range(17)]
# マックス桁数とその数の個数
for i in range(1, 17):
    keta_mat[i] = 9 * (10 ** (i - 1))

# 桁数
max_k = int(log10(N)) + 1

# max_k桁 の個数
max_keta_num = N - 10 ** (max_k - 1) + 1

ans = ((max_k - 1) // 3) * max_keta_num

for i in range(max_k - 1, 0, -1):
    ans += ((i - 1) // 3) * keta_mat[i]

print(ans)
