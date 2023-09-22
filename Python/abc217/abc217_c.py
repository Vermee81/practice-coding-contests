# https://atcoder.jp/contests/abc217/tasks/abc217_c
N = int(input())
p_arr = list(map(int, input().split()))
q_arr = [0] * N
for i, p in enumerate(p_arr):
    q_arr[p - 1] = i + 1

ans = " ".join([str(e) for e in q_arr])
print(ans)
