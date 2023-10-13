# https://atcoder.jp/contests/abc115/tasks/abc115_c
N, K = map(int, input().split())
h_arr = [int(input()) for _ in range(N)]
h_arr.sort()
ans = 10**9
for i in range(N - K + 1):
    left = i
    right = left + K - 1
    diff = h_arr[right] - h_arr[left]
    ans = min(ans, diff)
print(ans)
