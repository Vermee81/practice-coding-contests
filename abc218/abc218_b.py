# https://atcoder.jp/contests/abc218/tasks/abc218_b
alphabet = 'abcdefghijklmnopqrstuvwxyz'
p_arr = list(map(int, input().split()))
ans_list = []
for p in p_arr:
    ans_list.append(alphabet[p - 1])

ans = "".join(ans_list)
print(ans)
