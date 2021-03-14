# https://atcoder.jp/contests/abc195/tasks/abc195_d
N, M, Q = list(map(int, input().split()))
wv_arr = []
for _ in range(N):
    w, v = list(map(int, input().split()))
    wv_arr.append([w, v])
# 価値が大きい順に並び替える
wv_arr = sorted(wv_arr, key=lambda x: x[1], reverse=True)
x_arr = list(map(int, input().split()))

for _ in range(Q):
    l, r = list(map(int, input().split()))
    r_x_arr = []
    ans = 0

    # 箱を取り除く
    for i, x in enumerate(x_arr):
        if l-1 <= i <= r-1:
            continue
        r_x_arr.append(x)
    r_x_arr.sort()

    # 埋まってる箱に目印をつけるための配列
    rx_memo = [0 for _ in range(len(r_x_arr))]

    for wv in wv_arr:
        for i, rx in enumerate(r_x_arr):
            if wv[0] <= rx and rx_memo[i] == 0:
                ans += wv[1]
                rx_memo[i] = -1
                break
    print(ans)

