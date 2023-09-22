# https://atcoder.jp/contests/abc148/tasks/abc148_a
not_list = [int(input()) for _ in range(2)]
ans_list = [i for i in [1, 2, 3] if i not in not_list]
print(ans_list[0])
