# https://atcoder.jp/contests/abc209/tasks/abc209_b
N, X = map(int, input().split())
a_arr = list(map(int, input().split()))
total = 0
for i, a in enumerate(a_arr):
    if i % 2 == 1:
        total += (a - 1)
        continue
    total += a
ans = 'Yes' if total <= X else 'No'
print(ans)
