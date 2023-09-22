# https://atcoder.jp/contests/abc077/tasks/arc084_a
N = int(input())
a_arr = list(map(int, input().split()))
a_arr.sort()
b_arr = list(map(int, input().split()))
c_arr = list(map(int, input().split()))
c_arr.sort()


def find_least_idx(num: int, lst: list) -> int:
    n = len(lst)
    left = 0
    right = n - 1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] > num:
            right = mid
            continue
        left = mid + 1
    return right


def find_most_idx(num: int, lst: list) -> int:
    n = len(lst)
    left = 0
    right = n - 1
    while left < right:
        mid = (left + right) // 2 + 1
        if lst[mid] < num:
            left = mid
            continue
        right = mid - 1
    return left


total = 0

for b in b_arr:
    if a_arr[0] >= b:
        continue
    if c_arr[N - 1] <= b:
        continue
    a_most = find_most_idx(b, a_arr)
    c_least = find_least_idx(b, c_arr)
    total += (a_most + 1) * (N - c_least)

print(total)

