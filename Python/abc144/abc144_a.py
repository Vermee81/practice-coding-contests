# https://atcoder.jp/contests/abc144/tasks/abc144_a
A, B = map(int, input().split())
ans = A * B if A <= 9 and B <= 9 else -1
print(ans)
