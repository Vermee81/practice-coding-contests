# https://atcoder.jp/contests/abc200/tasks/abc200_c
N = int(input())
a_arr = list(map(int, input().split()))
amari = [0 for i in range(200)]
for a in a_arr:
    amari[a % 200] += 1

ans = 0
for i in range(200):
    ans += (amari[i] * (amari[i] - 1)) // 2

print(ans)
