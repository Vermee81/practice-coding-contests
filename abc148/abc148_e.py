# https://atcoder.jp/contests/abc148/tasks/abc148_e
N = int(input())
if N % 2 == 1:
    print(0)
    exit()

ans = 0

waru = 5

while waru <= N:
    ans += N // (waru * 2)
    waru *= 5

print(ans)






