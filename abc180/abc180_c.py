# https://atcoder.jp/contests/abc180/tasks/abc180_c
N = int(input())


def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


ans_list = make_divisors(N)
for a in ans_list:
    print(a)
