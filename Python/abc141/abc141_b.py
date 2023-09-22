# https://atcoder.jp/contests/abc141/tasks/abc141_b
S = input()
for i, l in enumerate(S):
    if (i + 1) % 2 == 1:
        if not(l in ['R', 'U', 'D']):
            print('No')
            exit()
    else:
        if not (l in ['L', 'U', 'D']):
            print('No')
            exit()

print('Yes')
