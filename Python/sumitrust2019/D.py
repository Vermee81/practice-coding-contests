# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d
N = int(input())
S = input()
ans_set = set()
memo1 = set()
memo2 = set()
for i in range(N-2):
    if S[i] in memo1:
        continue
    memo1.add(S[i])
    for j in range(i+1, N-1):
        keta = f"{S[i]}{S[j]}"
        if keta in memo2:
            continue
        memo2.add(keta)
        for k in range(j+1, N):
            ans_set.add(f"{S[i]}{S[j]}{S[k]}")
print(len(ans_set))

