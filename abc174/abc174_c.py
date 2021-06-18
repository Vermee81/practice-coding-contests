# https://atcoder.jp/contests/abc174/tasks/abc174_c
K = int(input())
if K == 1:
    print(1)
    exit()
memo = [0 for _ in range(K + 1)]
memo[1] = 7 % K
for i in range(2, K + 1):
    memo[i] = (memo[i - 1] * 10 + 7) % K

for i in range(1, K + 1):
    if memo[i] == 0:
        print(i)
        exit()

print(-1)
