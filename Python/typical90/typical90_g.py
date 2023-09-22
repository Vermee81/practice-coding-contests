# https://atcoder.jp/contests/typical90/tasks/typical90_g
N = int(input())
a_arr = list(map(int, input().split()))
a_arr.sort()
Q = int(input())

for _ in range(Q):
    b = int(input())
    if b >= a_arr[N - 1]:
        print(abs(a_arr[N - 1] - b))
        continue
    if b <= a_arr[0]:
        print(abs(a_arr[0] - b))
        continue

    left = -1
    right = N

    minimum = 10**9

    while right - left > 1:
        mid = (right + left) // 2
        if a_arr[mid] <= b:
            left = mid
            minimum = min(minimum, abs(a_arr[left] - b))
        else:
            right = mid
            minimum = min(minimum, abs(a_arr[right] - b))

    print(minimum)


