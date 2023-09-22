# https://atcoder.jp/contests/abc171/tasks/abc171_e
N = int(input())
a_arr = list(map(int, input().split()))
first = 0
for i in range(1, N):
    first = first ^ a_arr[i]
all_base = first ^ a_arr[0]

ans = list()
ans.append(first)

for i in range(1, N):
    a = all_base ^ a_arr[i]
    ans.append(a)

ans_str = " ".join([str(s) for s in ans])
print(ans_str)
