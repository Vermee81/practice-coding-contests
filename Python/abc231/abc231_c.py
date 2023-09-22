# https://atcoder.jp/contests/abc231/tasks/abc231_c
N, Q = map(int, input().split())
a_arr = list(map(int, input().split()))
a_arr.sort()


def bin_search(x: int):
    low = 0
    high = N - 1
    if a_arr[high] < x:
        return N
    if a_arr[low] >= x:
        return 0
    while high - low > 1:
        mid = (high + low) // 2
        if a_arr[mid] < x:
            low = mid
        else:
            high = mid
    return high


for _ in range(Q):
    x = int(input())
    index = bin_search(x)
    print(N - index)
