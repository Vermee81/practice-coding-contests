# https://atcoder.jp/contests/abc194/tasks/abc194_c
N = int(input())
a_list = list(map(int, input().split()))

double_sum = 0
for a in a_list:
    double_sum += a**2

ans = N * double_sum - (sum(a_list)**2)

print(ans)