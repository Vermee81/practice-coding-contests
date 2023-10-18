# https://atcoder.jp/contests/abc170/tasks/abc170_b
X, Y = map(int, input().split())
ans = "No"
for i in range(101):
    for j in range(101):
        if i + j == X and 2 * i + 4 * j == Y:
            ans = "Yes"
print(ans)

