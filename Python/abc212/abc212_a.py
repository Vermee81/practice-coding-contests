# https://atcoder.jp/contests/abc212/tasks/abc212_a
A, B = map(int, input().split())
if 0 < A:
    if B == 0:
        print('Gold')
        exit()
    if 0 < B:
        print('Alloy')
        exit()
print('Silver')
