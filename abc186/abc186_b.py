# https://atcoder.jp/contests/abc186/tasks/abc186_b
H, W = list(map(int, input().split()))
blocks = []
for _ in range(H):
  row = list(map(int, input().split()))
  blocks.append(row)

min_val = 101
total = 0
for row in blocks:
  min_val = min(min_val, min(row))
  total += sum(row)

ans = total - (min_val * H * W)
print(ans)