# https://atcoder.jp/contests/abc209/tasks/abc209_a
A, B = map(int, input().split())
ans = (B - A + 1) if B >= A else 0
print(ans)

