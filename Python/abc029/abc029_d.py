# https://atcoder.jp/contests/abc029/tasks/abc029_d
N = int(input())
ans = 0
for k in range(10):
    cycle = 10 ** (k + 1)
    unit = (N + 1) // cycle
    ans += unit * (10 ** k)

    remainder = (N + 1) % cycle
    remainder -= (10 ** k)
    remainder = max(remainder, 0)
    ans += min(remainder, 10 ** k)

print(ans)
