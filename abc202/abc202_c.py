# https://atcoder.jp/contests/abc202/tasks/abc202_c
N = int(input())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))
c_arr = list(map(int, input().split()))
counter = [0 for _ in range(N + 1)]
for c in c_arr:
    counter[b_arr[c - 1]] += 1

ans = 0
for a in a_arr:
    ans += counter[a]
print(ans)
