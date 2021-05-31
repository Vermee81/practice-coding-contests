N, K = map(int, input().split())
a = (N * (N + 1) // 2) * 100 * K
b = (K * (K + 1) // 2) * N
print(a + b)

