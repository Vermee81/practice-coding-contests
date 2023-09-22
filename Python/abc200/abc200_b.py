# https://atcoder.jp/contests/abc200/tasks/abc200_b
N, K = map(int, input().split())

for _ in range(K):
    if N % 200 == 0:
        N /= 200
        N = int(N)
    else:
        newN = "".join([str(N), "200"])
        N = int(newN)
print(N)
