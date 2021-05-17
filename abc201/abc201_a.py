# https://atcoder.jp/contests/abc201/tasks/abc201_a
a_arr = list(map(int, input().split()))
a_arr.sort()
ans = 'No'
if (a_arr[0] - a_arr[1]) == (a_arr[1] - a_arr[2]):
    ans = 'Yes'
print(ans)
