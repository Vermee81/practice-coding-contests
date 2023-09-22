# https://atcoder.jp/contests/abc103/tasks/abc103_d
N, M = list(map(int, input().split()))
ab_list = []
for _ in range(M):
    a, b = list(map(int, input().split()))
    ab_list.append([a, b])

ab_list = sorted(ab_list, key=lambda x: x[1])
min_range = [ab_list[0][0], ab_list[0][1]]
ans = 1
for ab in ab_list:
    if ab[0] < min_range[1]:
        min_range[0] = max(min_range[0], ab[0])
        continue
    min_range = [ab[0], ab[1]]
    ans += 1
print(ans)

