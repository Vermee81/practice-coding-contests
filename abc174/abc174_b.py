# https://atcoder.jp/contests/abc174/tasks/abc174_b
N, D = map(int, input().split())
zahyo = []
ans = 0
for _ in range(N):
    x, y = map(int, input().split())
    if D**2 >= (x**2 + y**2):
        ans += 1
print(ans)
