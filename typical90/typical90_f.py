# https://atcoder.jp/contests/typical90/tasks/typical90_f
N, K = map(int, input().split())
S = input()
alphabet = [s for s in 'abcdefghijklmnopqrstuvwxyz']
c = [[-1 for _ in range(N + 1)] for _ in range(26)]

for i, l in enumerate(alphabet):
    for j in range(N - 1, -1, -1):
        if S[j] == l:
            c[i][j] = j
            continue

        if j + 1 <= N and c[i][j + 1] != -1:
            c[i][j] = c[i][j + 1]

ans = ""
start = 0
for k in range(K):
    for j in range(26):
        if c[j][start] != -1 and (N - c[j][start]) >= (K - k):
            ans += alphabet[j]
            start = c[j][start] + 1
            break
print(ans)
