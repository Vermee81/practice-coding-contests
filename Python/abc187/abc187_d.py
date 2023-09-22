# https://atcoder.jp/contests/abc187/tasks/abc187_d
N = int(input())
b_score = 0
ab_arr = []
for _ in range(N):
    a, b = map(int, input().split())
    ab_arr.append(2 * a + b)
    b_score += a

ab_arr.sort()

a_score = 0
ans = 0
while b_score >= 0:
    b_score -= ab_arr.pop()
    ans += 1

print(ans)
