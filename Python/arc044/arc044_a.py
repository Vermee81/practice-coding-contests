# https://atcoder.jp/contests/arc044/tasks/arc044_a
from math import sqrt
N = int(input())

if N == 1:
    print('Not Prime')
    exit()

if N == 2:
    print('Prime')
    exit()

if N % 2 == 0:
    print('Not Prime')
    exit()

for i in range(3, int(sqrt(N)) + 1, 2):
    if N % i == 0:
        first_keta = N % 10
        if first_keta % 2 != 0 and first_keta != 5 and N % 3 != 0:
            print('Prime')
            exit()
        print('Not Prime')
        exit()

print('Prime')
