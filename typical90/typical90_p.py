# https://atcoder.jp/contests/typical90/tasks/typical90_p
N = int(input())
A, B, C = map(int, input().split())

ans = 10**9

for x in range(10000):
    for y in range(10000):
        a_b_sum = A * x + B * y
        if (N - a_b_sum) % C != 0 or N < a_b_sum:
            continue
        z = (N - a_b_sum) // C
        ans = min(x + y + z, ans)

print(ans)
