# https://atcoder.jp/contests/abc186/tasks/abc186_c
N = int(input())
counter = 0
for i in range(1, N + 1):
    str_i = str(i)
    oct_str_i = oct(i)
    if '7' in str_i or '7' in oct_str_i:
        counter += 1

print(N - counter)
