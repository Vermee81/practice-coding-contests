# https://atcoder.jp/contests/abc122/tasks/abc122_c
N, Q = map(int, input().split())
S = input()
acc = [0 for _ in range(N + 1)]
for i in range(1, N):
    if S[i - 1] == 'A' and S[i] == 'C':
        acc[i] = acc[i - 1] + 1
        continue
    acc[i] = acc[i - 1]

for _ in range(Q):
    l, r = map(int, input().split())
    print(acc[r - 1] - acc[l - 1])
