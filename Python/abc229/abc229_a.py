# https://atcoder.jp/contests/abc229/tasks/abc229_a
S, T, X = map(int, input().split())
if S == T:
    print("No")
    exit()

if S > T:
    ans = "Yes" if X >= S or X < T else "No"
    print(ans)
    exit()

ans = "Yes" if S <= X < T else "No"
print(ans)
