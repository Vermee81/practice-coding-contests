# https://atcoder.jp/contests/jsc2021/tasks/jsc2021_c
A, B = map(int, input().split())
ans = 1
for c in range(2, B + 1):
    count = B // c - ((A - 1) // c)
    if count >= 2:
        ans = max(ans, c)
print(ans)
