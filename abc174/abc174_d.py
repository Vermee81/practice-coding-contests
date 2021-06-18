# https://atcoder.jp/contests/abc174/tasks/abc174_d
N = int(input())
c_arr = list(input())
if not 'R' in c_arr:
    print(0)
    exit()
ans = 0
R_num, W_num = 0, 0
for c in c_arr:
    if c == 'W':
        W_num += 1
    if c == 'R':
        R_num += 1
shikii_list = [0 for _ in range(N)]
shikii_list[0] = R_num
shikii_left_W_num = 0
shikii_right_R_num = R_num
for s in range(N):
    if c_arr[s] == 'W':
        shikii_left_W_num += 1
    if c_arr[s] == 'R':
        shikii_right_R_num -= 1
    shikii_list[s] = max(shikii_left_W_num, shikii_right_R_num)
print(min(shikii_list))

