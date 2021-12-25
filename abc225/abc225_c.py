# https://atcoder.jp/contests/abc225/tasks/abc225_c
N, M = map(int, input().split())
b_arr = []
for _ in range(N):
    b_arr.append(list(map(lambda x: int(x) - 1, input().split())))

for i in range(N):
    for j in range(M):
        now_column = b_arr[i][j] % 7
        if now_column != (b_arr[0][0] % 7) + j:
            print('No')
            exit()
        if j > 0:
            if b_arr[i][j - 1] != b_arr[i][j] - 1:
                print('No')
                exit()
        if i > 0:
            if b_arr[i - 1][j] != b_arr[i][j] - 7:
                print('No')
                exit()

print('Yes')
