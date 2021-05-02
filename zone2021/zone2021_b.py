# https://atcoder.jp/contests/zone2021/tasks/zone2021_b
N, D, H = map(int, input().split())
ans = 0
for i in range(N):
    d, h = map(int, input().split())
    b = (D*h - d*H) / (D - d)
    ans = max(ans, b)
print(ans)
