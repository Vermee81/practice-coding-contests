# https://atcoder.jp/contests/abc213/tasks/abc213_b
N = int(input())
a_arr = list(map(int, input().split()))
num_score_list = []
for i, a in enumerate(a_arr):
    num_score_list.append([i + 1, a])

sorted_ns_list = sorted(num_score_list, key=lambda x: x[1])
print(sorted_ns_list[N - 2][0])
