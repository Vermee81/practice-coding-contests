# https://atcoder.jp/contests/abc182/tasks/abc182_d
N = int(input())
a_arr = list(map(int, input().split()))
if N == 1:
    print(max(0, a_arr[0]))
    exit()
ans = 0
zahyo = 0
# cum[max_point][累積]
cum = [[0, 0] for _ in range(N + 1)]
cum[0][0] = a_arr[0]
cum[0][1] = a_arr[0]
for i in range(1, N):
    cum[i][1] = cum[i - 1][1] + a_arr[i]
    cum[i][0] = max(cum[i - 1][0], cum[i][1])

for c in cum:
    ans = max(zahyo + c[0], ans)
    zahyo += c[1]
print(ans)
