# https://atcoder.jp/contests/abc219/tasks/abc219_a
X = int(input())
if X >= 90:
    print('expert')
    exit()

if 70 <= X < 90:
    print(90 - X)
    exit()

if 40 <= X < 70:
    print(70 - X)
    exit()

print(40 - X)
