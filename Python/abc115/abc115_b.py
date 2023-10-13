# https://atcoder.jp/contests/abc115/tasks/abc115_b
N = int(input())
p_list = [int(input()) for i in range(N)]

max_p = max(p_list)
ans = sum(p_list) - max_p // 2
print(ans)

