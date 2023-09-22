# https://atcoder.jp/contests/abc195/tasks/abc195_b
A, B, W = list(map(int, input().split()))
W *= 1000

ans_num = []
for i in range(1, 10**6 + 1):
    if A <= W/i <= B:
        ans_num.append(i)
if ans_num:
    print(min(ans_num), max(ans_num))
    exit()
print('UNSATISFIABLE')
