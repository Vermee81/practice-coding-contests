# https://atcoder.jp/contests/jsc2021/tasks/jsc2021_d
N, P = map(int, input().split())
MOD = 10**9 + 7


# a^n modを計算する
def modpow(a: int, n: int, m: int):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % m
        a = a * a % m
        n = n >> 1
    return res


ans = ((P - 1) % MOD) * modpow((P - 2), (N - 1), MOD)
print(ans % MOD)
