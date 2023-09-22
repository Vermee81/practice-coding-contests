H, W = map(int, input().split())
field = [[str(i) for i in input()] for _ in range(H)]
count = 0
for x in range(W-1):
    for y in range(H-1):
        black_num = 0
        for x1, y1 in [(x, y), (x+1, y), (x, y+1), (x+1, y+1)]:
            if field[y1][x1] == '#':
                black_num += 1
        if black_num % 2 == 1:
            count += 1
print(count)
