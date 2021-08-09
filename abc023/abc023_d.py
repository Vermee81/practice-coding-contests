# https://atcoder.jp/contests/abc023/tasks/abc023_d
N = int(input())
h_list = []
s_list = []
for _ in range(N):
    h, s = map(int, input().split())
    h_list.append(h)
    s_list.append(s)

ok = max(h_list) + max(s_list) * (N - 1)
ng = max(h_list) - 1

while ok - ng > 1:
    mid = (ok + ng) // 2
    hantei = True
    # 各風船を割るまでの時間制限
    t = [0 for _ in range(N)]
    for i in range(N):
        if mid < h_list[i]:
            hantei = False
            break
        t[i] = (mid - h_list[i]) // s_list[i]
    t.sort()
    for i, time in enumerate(t):
        if time < i:
            hantei = False
            break

    if hantei:
        ok = mid
    else:
        ng = mid

print(ok)
