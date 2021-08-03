# https://atcoder.jp/contests/abc205/tasks/abc205_b
N = int(input())
a_arr = list(map(int, input().split()))
a_arr.sort()
right_arr = [i for i in range(1, N + 1)]
if a_arr == right_arr:
    print('Yes')
    exit()
print('No')
