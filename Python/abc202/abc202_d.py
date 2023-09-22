# https://atcoder.jp/contests/abc202/tasks/abc202_d
A, B, K = map(int, input().split())

# memo[a][b] aがa個, bがb個の時の場合の数
memo = [[0 for _ in range(31)] for _ in range(31)]
memo[0][0] = 1
for i in range(A + 1):
    for j in range(B + 1):
        if i == 0:
            memo[i][j] = 1
            continue
        if j == 0:
            memo[i][j] = 1
            continue
        memo[i][j] += memo[i][j - 1] + memo[i - 1][j]


def get_S(a, b, k):
    if a == 0:
        return "b" * b
    if b == 0:
        return "a" * a
    if memo[a - 1][b] >= k:
        return "a" + get_S(a - 1, b, k)
    if memo[a - 1][b] < k:
        return "b" + get_S(a, b - 1, k - memo[a - 1][b])


print(get_S(A, B, K))
