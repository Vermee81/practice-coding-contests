# https://atcoder.jp/contests/abc194/tasks/abc194_d
N = int(input())
ans = 0
for i in range(1, N):
    ans += N / i
print(ans)