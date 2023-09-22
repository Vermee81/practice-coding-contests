# https://atcoder.jp/contests/abc225/tasks/abc225_b
N = int(input())
hen_count = [0] * N
for _ in range(N - 1):
    a, b = map(int, input().split())
    hen_count[a - 1] += 1
    hen_count[b - 1] += 1

for h in hen_count:
    if h == N - 1:
        print("Yes")
        exit()

print("No")
