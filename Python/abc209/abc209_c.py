# https://atcoder.jp/contests/abc209/tasks/abc209_c
N = int(input())
c_arr = list(map(int, input().split()))
c_arr.sort()
ans = 1
R = 10**9 + 7
for i in range(N):
    ans = ans * (c_arr[i] - i) % R
print(ans % R)
