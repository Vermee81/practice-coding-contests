# https://atcoder.jp/contests/abc108/tasks/abc108_b
x1, y1, x2, y2 = map(int, input().split())
diff_x = abs(x2 - x1)
diff_y = abs(y2 - y1)

if diff_x == 0:
    if y2 > y1:
        diff_y *= -1
    print(x2 + diff_y, y2, x1 + diff_y, y1)
    exit()

if diff_y == 0:
    if x2 < x1:
        diff_x *= -1
    print(x2, y1 + diff_x, x1, y2 + diff_x)
    exit()

if y2 > y1:
    diff_y *= -1
if x2 < x1:
    diff_x *= -1
print(x2 + diff_y, y2 + diff_x, x1 + diff_y, y1 + diff_x)

