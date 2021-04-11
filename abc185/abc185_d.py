# https://atcoder.jp/contests/abc185/tasks/abc185_d
from math import ceil
N, M = map(int, input().split())
if M == 0:
    print(1)
    exit()
a_arr = list(map(int, input().split()))
a_arr.sort()
blanks = [0]
for i in range(M):
    if i == 0:
        blanks.append(a_arr[i] - 1)
        continue
    blanks.append(a_arr[i] - a_arr[i - 1] - 1)
blanks.append(N - a_arr[-1])
minimum = N
for b in blanks:
    if b == 0:
        continue
    minimum = min(minimum, b)

ans = 0
for b in blanks:
    ans += ceil(b / minimum)
print(ans)
