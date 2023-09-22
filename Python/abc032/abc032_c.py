# https://atcoder.jp/contests/abc032/tasks/abc032_c
N, K = map(int, input().split())

s_arr = []
for _ in range(N):
    s = int(input())
    if s == 0:
        print(N)
        exit()
    s_arr.append(s)

ans = 0
right = 0
rui = 1
for i in range(N):
    while right < N and rui * s_arr[right] <= K:
        rui *= s_arr[right]
        right += 1
    ans = max(ans, right - i)
    if i == right:
        right += 1
    else:
        rui /= s_arr[i]

print(ans)
