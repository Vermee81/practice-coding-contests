# https://atcoder.jp/contests/abc064/tasks/abc064_a
r, g, b = map(int, input().split())
ans = 'YES' if (r * 100 + g * 10 + b) % 4 == 0 else 'NO'
print(ans)
