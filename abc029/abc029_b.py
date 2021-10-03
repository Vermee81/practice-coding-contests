# https://atcoder.jp/contests/abc029/tasks/abc029_b
ans = 0
for _ in range(12):
    str = input()
    if str.find('r') != -1:
        ans += 1

print(ans)
