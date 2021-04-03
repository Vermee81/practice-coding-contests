# https://atcoder.jp/contests/abc177/tasks/abc177_b
S = input()
T = input()
ans = len(T) + 1
for i in range(len(S) - len(T) + 1):
    c = 0
    for j, t in enumerate(T):
        if i + j < len(S) and t != S[i + j]:
            c += 1
    ans = min(ans, c)
print(ans)
