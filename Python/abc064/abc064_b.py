# https://atcoder.jp/contests/abc064/tasks/abc064_b
N = int(input())
a_arr = list(map(int, input().split()))
print(max(a_arr) - min(a_arr))
