# https://atcoder.jp/contests/abc229/tasks/abc229_c
N, W = map(int, input().split())
ab_arr = []
for _ in range(N):
    a, b = map(int, input().split())
    ab_arr.append([a, b])

ab_arr.sort(reverse=True)

weight = 0
delicious_point = 0

for ab in ab_arr:
    p = ab[0]
    w = ab[1]
    if weight + w <= W:
        weight += w
        delicious_point += w * p
        continue
    nokori = W - weight
    weight += nokori
    delicious_point += nokori * p


print(delicious_point)
