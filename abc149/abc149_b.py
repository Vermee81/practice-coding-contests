# https://atcoder.jp/contests/abc149/tasks/abc149_b
A, B, K = list(map(int, input().split()))
if A >= K:
    A = A - K
    print(f"{A} {B}")
    exit()
K = K - A
if B > K:
    B = B - K
    print(f"0 {B}")
    exit()
print("0 0")
