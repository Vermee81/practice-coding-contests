# https://atcoder.jp/contests/abc192/tasks/abc192_c
N, K = map(int, input().split())
ans = N
for _ in range(K):
    str_N = str(ans)
    g1 = int("".join(sorted(str_N, reverse=True)))
    g2 = int("".join(sorted(str_N)))
    ans = g1 - g2
print(ans)
