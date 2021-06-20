from math import floor
N = int(input())
if floor(N * 1.08) == 206:
    print('so-so')
    exit()
ans = 'Yay!' if floor(N * 1.08) < 206 else ':('
print(ans)
