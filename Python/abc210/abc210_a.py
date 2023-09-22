# https://atcoder.jp/contests/abc210/tasks/abc210_a
N, A, X, Y = map(int, input().split())
total = 0
if N <= A:
    print(X * N)
    exit()
print(X * A + Y * (N - A))
