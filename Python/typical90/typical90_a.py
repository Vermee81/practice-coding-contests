# https://atcoder.jp/contests/typical90/tasks/typical90_a
N, L = map(int, input().split())
K = int(input())
a_arr = list(map(int, input().split()))
ans = 0
right = L + 1
left = -1
while right - left > 1:
    mid = (right + left) // 2
    # K + 1個以上の長さmid以上のピースに分割しきれるかどうか
    bar_len = 0
    split_count = 0
    previous = 0
    hantei = False
    for i in range(N):
        bar_len = a_arr[i] - previous
        if bar_len >= mid:
            previous = a_arr[i]
            split_count += 1
            bar_len = 0
    bar_len = L - previous
    if bar_len >= mid:
        split_count += 1

    if split_count > K:
        left = mid
    else:
        right = mid


print(left)



