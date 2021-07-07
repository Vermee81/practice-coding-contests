# https://atcoder.jp/contests/abc066/tasks/arc077_a
from collections import deque
N = int(input())
a_arr = list(map(int, input().split()))
b_arr = deque()
flip_flag = False
b_arr.append(a_arr[0])

for i in range(1, N):
    if flip_flag:
        b_arr.appendleft(a_arr[i])
    else:
        b_arr.append(a_arr[i])
    flip_flag = not flip_flag

if flip_flag:
    b_arr.reverse()

ans = " ".join([str(i) for i in b_arr])
print(ans)
