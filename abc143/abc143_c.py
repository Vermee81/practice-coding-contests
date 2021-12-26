# https://atcoder.jp/contests/abc143/tasks/abc143_c
N = int(input())
S = input()

ans_list = [S[0]]
before = S[0]
current_s = S[0]

for i in range(1, N):
    current_s = S[i]
    if current_s != before:
        ans_list.append(current_s)
    before = current_s

print(len(ans_list))
