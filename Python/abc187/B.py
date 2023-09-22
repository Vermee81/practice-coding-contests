N = int(input())
coord = []
counter = 0
for _ in range(N):
    x, y = list(map(int, input().split()))
    coord.append((x, y))
for i in range(N - 1):
    for j in range(i+1, N):
        slope_top = coord[i][1] - coord[j][1]
        slope_bottom = coord[i][0] - coord[j][0]
        slope = slope_top / slope_bottom
        if -1 <= slope <= 1:
            counter += 1
print(counter)
