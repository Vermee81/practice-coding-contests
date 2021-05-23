# https://atcoder.jp/contests/abc131/tasks/abc131_c
from math import gcd
A, B, C, D = map(int, input().split())


def lcm(a, b):
    return a // gcd(a, b) * b


LCM = lcm(C, D)
# x % c != 0 and x % d != 0
# not(x % c == 0 or x % d == 0)
# 1~AでCでもDでも割り切れない個数 = (1~Aの個数) - ((1~AでCで割り切れる) + (1~AでDで割り切れる) - (1~AでCでもDでも割り切れる))
# 1~BでCでもDでも割り切れない個数 = (1~Bの個数) - ((1~BでCで割り切れる) + (1~BでDで割り切れる) - (1~BでCでもDでも割り切れる))
one_to_A = (A - 1) - (((A - 1) // C) + ((A - 1) // D) - ((A - 1) // LCM))
one_to_B = B - ((B // C) + (B // D) - (B // LCM))
print(one_to_B - one_to_A)
