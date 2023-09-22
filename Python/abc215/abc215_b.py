# https://atcoder.jp/contests/abc215/tasks/abc215_b
N = int(input())
ans = 0
while N > 1:
    ans += 1
    N //= 2
print(ans)
