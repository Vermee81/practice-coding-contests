# https://atcoder.jp/contests/abc184/tasks/abc184_b
N, X = list(map(int, input().split()))
S = input()
score = X
for s in S:
    if s == 'x' and score > 0:
        score -= 1
        continue
    if s == 'o':
        score += 1
        continue
print(score)