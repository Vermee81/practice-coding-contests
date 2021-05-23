# https://atcoder.jp/contests/abc131/tasks/abc131_b
N, L = map(int, input().split())

aji = []
for n in range(1, N + 1):
    aji.append(L + n - 1)

ans = 0
min_diff = 10**9 + 7
total = sum(aji)

for a in aji:
    diff = abs(total - (total - a))
    if min_diff > diff:
        min_diff = diff
        ans = total - a
print(ans)
