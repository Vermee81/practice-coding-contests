# https://atcoder.jp/contests/arc121/tasks/arc121_a
N = int(input())
houses = []
for _ in range(N):
    x, y = map(int, input().split())
    houses.append([x, y])


def find_second(house_list: list) -> int:
    n = len(house_list)
    first_dist = -1
    second_dist = -1
    for j in range(n - 1):
        for k in range(j + 1, n):
            dist = max(abs(house_list[j][0] - house_list[k][0]), abs(house_list[j][1] - house_list[k][1]))
            if dist > first_dist:
                second_dist = first_dist
                first_dist = dist
                continue
            elif first_dist >= dist > second_dist:
                second_dist = dist
    return second_dist


if N < 9:
    print(find_second(houses))
    exit()


max_x_idx, min_x_idx = 0, 0
max_y_idx, min_y_idx = 0, 0
second_large_x_idx, second_small_x_idx = 0, 0
second_large_y_idx, second_small_y_idx = 0, 0

for i, h in enumerate(houses):
    if houses[max_x_idx][0] >= h[0] > houses[second_large_x_idx][0]:
        second_large_x_idx = i
    if houses[max_y_idx][1] >= h[1] > houses[second_large_y_idx][1]:
        second_large_y_idx = i
    if houses[max_x_idx][0] < h[0]:
        second_large_x_idx = max_x_idx
        max_x_idx = i
    if houses[max_y_idx][1] < h[1]:
        second_large_y_idx = max_y_idx
        max_y_idx = i
    if houses[min_x_idx][0] <= h[0] < houses[second_small_x_idx][0]:
        second_small_x_idx = i
    if houses[min_y_idx][1] <= h[1] < houses[second_small_y_idx][1]:
        second_small_y_idx = i
    if houses[min_x_idx][0] > h[0]:
        second_small_x_idx = min_x_idx
        min_x_idx = i
    if houses[min_y_idx][1] > h[1]:
        second_small_y_idx = min_y_idx
        min_y_idx = i

limit_houses_idx = [max_y_idx, max_x_idx, min_y_idx, min_x_idx,
                    second_small_y_idx, second_small_x_idx, second_large_x_idx, second_large_y_idx]
limit_houses_set = set(limit_houses_idx)
limit_houses_idx = list(limit_houses_set)

limit_houses_list = []

for lhi in limit_houses_idx:
    limit_houses_list.append(houses[lhi])


print(find_second(limit_houses_list))
