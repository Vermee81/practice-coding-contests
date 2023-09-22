# https://atcoder.jp/contests/abc205/tasks/abc205_c
A, B, C = map(int, input().split())

if A > 0 and B > 0:
    if A > B:
        print('>')
        exit()
    if A < B:
        print('<')
        exit()

if A < 0 and B < 0:
    if C % 2 == 0:
        if A > B:
            print('>')
            exit()
        if A < B:
            print('<')
            exit()
    if A > B:
        print('<')
        exit()
    if A < B:
        print('>')
        exit()


if A < 0 < B:
    if C % 2 == 0:
        if abs(A) > B:
            print('>')
            exit()
        if abs(A) < B:
            print('<')
            exit()
    if C % 2 != 0:
        print('<')
        exit()

if B < 0 < A:
    if C % 2 == 0:
        if A > abs(B):
            print('>')
            exit()
        if A < abs(B):
            print('<')
            exit()
    if C % 2 != 0:
        print('>')
        exit()

if A == 0:
    if B < 0:
        if C % 2 == 0:
            print('<')
            exit()
        if C % 2 != 0:
            print('>')
            exit()
    if B > 0:
        print('<')
        exit()

if B == 0:
    if A < 0:
        if C % 2 == 0:
            print('>')
            exit()
        if C % 2 != 0:
            print('<')
            exit()
    if A > 0:
        print('>')
        exit()

print('=')
