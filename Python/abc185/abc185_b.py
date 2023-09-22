# https://atcoder.jp/contests/abc185/tasks/abc185_b
N, M, T = map(int, input().split())
ab_arr = [[int(i) for i in input().split()] for _ in range(M)]
n = N
time = 0
for ab in ab_arr:
    a = ab[0]
    b = ab[1]
    n -= (a - time)
    time = a
    if n <= 0:
        print('No')
        exit()
    time = b
    n += (b - a)
    if n > N:
        n = N

if n - T + time > 0:
    print('Yes')
    exit()
print('No')
