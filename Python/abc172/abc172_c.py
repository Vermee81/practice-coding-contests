# https://atcoder.jp/contests/abc172/tasks/abc172_c
N, M, K = map(int, input().split())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

cum_a_time = [0]
cum_b_time = [0]
for i in range(len(a_arr)):
    cum_a_time.append(cum_a_time[i] + a_arr[i])
for i in range(len(b_arr)):
    cum_b_time.append(cum_b_time[i] + b_arr[i])

ans = 0

for i, a in enumerate(cum_a_time):
    j = max(ans - i, 0)
    while j < len(cum_b_time) and K >= a + cum_b_time[j]:
        ans = max(ans, i + j)
        j += 1

print(ans)
