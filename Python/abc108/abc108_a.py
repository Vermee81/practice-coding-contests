# https://atcoder.jp/contests/abc108/tasks/abc108_a
K = int(input())
if K % 2 == 0:
    print(K//2 * K//2)
    exit()
print(K//2 * (K//2 + 1))
