# https://atcoder.jp/contests/typical90/tasks/typical90_j
N = int(input())
rui = [([0] * (N + 1)) for _ in range(2)]
for i in range(N):
    c, p = map(int, input().split())
    rui[c - 1][i + 1] = rui[c - 1][i] + p
    rui[c % 2][i + 1] = rui[c % 2][i]

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(rui[0][r] - rui[0][l - 1], rui[1][r] - rui[1][l - 1])



