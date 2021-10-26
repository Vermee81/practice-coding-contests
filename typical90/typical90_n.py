# https://atcoder.jp/contests/typical90/tasks/typical90_n
N = int(input())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))
a_arr.sort()
b_arr.sort()
ans = 0
for a, b in zip(a_arr, b_arr):
    ans += abs(a - b)
print(ans)
