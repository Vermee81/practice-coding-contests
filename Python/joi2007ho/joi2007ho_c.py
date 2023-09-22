import itertools

N = int(input())
coordinates = []
max_area = 0
for _ in range(N):
    x, y = list(map(int, input().split()))
    coordinates.append((x, y))
coordinates = set(coordinates)

for p, q in itertools.combinations(coordinates, 2):
    x1, y1 = p
    x2, y2 = q
    if (x1 - y2 + y1, y1 + x2 - x1) in coordinates and (x2 - y2 + y1, x2 + y2 - x1) in coordinates:
        area = (x1 - x2) ** 2 + (y1 - y2) ** 2
        max_area = max(max_area, area)
print(max_area)
