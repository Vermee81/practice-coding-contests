# https://atcoder.jp/contests/abc212/tasks/abc212_c
N, M = map(int, input().split())
a_arr = list(map(int, input().split()))
a_arr.sort()
b_arr = list(map(int, input().split()))
b_arr.sort()

ans = 10**10
i = 0
j = 0
while i < N and j < M:
    ans = min(ans, abs(a_arr[i] - b_arr[j]))
    if a_arr[i] > b_arr[j]:
        j += 1
    else:
        i += 1

print(ans)
