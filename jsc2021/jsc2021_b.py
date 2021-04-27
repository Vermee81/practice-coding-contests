# https://atcoder.jp/contests/jsc2021/tasks/jsc2021_b
N, M = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

ans_set1 = b_set - a_set
ans_set2 = a_set - b_set
ans_set = ans_set1 | ans_set2

ans_list = list(ans_set)
ans_list.sort()
ans = " ".join([str(i) for i in ans_list])
print(ans)
