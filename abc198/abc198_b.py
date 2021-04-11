# https://atcoder.jp/contests/abc198/tasks/abc198_b
N = input()

for i in range(11):
    add_0 = '0' * i
    n_str = add_0 + N
    if n_str == n_str[::-1]:
        print('Yes')
        exit()
print('No')
