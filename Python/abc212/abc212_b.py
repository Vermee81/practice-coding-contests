# https://atcoder.jp/contests/abc212/tasks/abc212_b
x_arr = [int(i) for i in input()]
ans = 'Strong'
if x_arr[0] == x_arr[1] == x_arr[2] == x_arr[3]:
    print('Weak')
    exit()
for i in range(3):
    if x_arr[i] == 9 and x_arr[i + 1] == 0:
        ans = 'Weak'
        continue
    if x_arr[i] + 1 == x_arr[i + 1]:
        ans = 'Weak'
        continue
    ans = 'Strong'
    break
print(ans)
