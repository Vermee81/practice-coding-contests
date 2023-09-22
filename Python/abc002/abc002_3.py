# https://atcoder.jp/contests/abc002/tasks/abc002_3
ax, ay, bx, by, cx, cy = map(int, input().split())
ans = (ax * by + ay * cx + bx * cy - ay * bx - ax * cy - by * cx) * 0.5
print(abs(ans))
# ax ay 1 ax ay
# bx by 1 bx by
# cx cy 1 cx cy
# ax * by + ay * cx + bx * cy - ay * bx - ax * cy - by * cx
