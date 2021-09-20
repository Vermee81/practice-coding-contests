# https://atcoder.jp/contests/abc219/tasks/abc219_b
S1 = input()
S2 = input()
S3 = input()
T = input()
my_dict = {'1': S1, '2': S2, '3': S3}
ans = ""
for t in T:
    ans = ans + my_dict[t]

print(ans)