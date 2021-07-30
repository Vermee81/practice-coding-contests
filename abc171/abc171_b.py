# https://atcoder.jp/contests/abc171/tasks/abc171_b
N, K = map(int, input().split())
p_arr = list(map(int, input().split()))
p_arr.sort()
ans = 0
for i in range(K):
    ans += p_arr[i]
print(ans)
