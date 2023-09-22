# https://atcoder.jp/contests/abc006/tasks/abc006_2
n = int(input())
MOD = 10 ** 4 + 7

if n in [1, 2]:
    print(0)
    exit()
if n == 3:
    print(1)
    exit()

tribo_memo = [0 for _ in range(n + 1)]
tribo_memo[3] = 1
for i in range(4, n + 1):
    tribo_memo[i] = ((tribo_memo[i - 1]) + (tribo_memo[i - 2]) + (tribo_memo[i - 3])) % MOD

print(tribo_memo[n])
