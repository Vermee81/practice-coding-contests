# https://atcoder.jp/contests/abc187/tasks/abc187_c
N = int(input())
b_set = set()
n_set = set()
for _ in range(N):
    s = input()
    if s[0] == '!':
        s_s = s[1:]
        b_set.add(s_s)
        continue
    n_set.add(s)

both = b_set & n_set
if len(both):
    print(both.pop())
    exit()
print('satisfiable')
