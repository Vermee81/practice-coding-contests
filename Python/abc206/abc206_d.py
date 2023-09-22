# https://atcoder.jp/contests/abc206/tasks/abc206_d
N = int(input())
a_arr = list(map(int, input().split()))
par = [i for i in range(max(a_arr) + 1)]


def root(x: int) -> int:
    if par[x] == x:
        return x
    par[x] = root(par[x])
    return par[x]


def unite(x: int, y: int):
    x = root(x)
    y = root(y)
    if x == y:
        return 0
    par[y] = x


ans = 0
for i in range(N):
    if root(a_arr[i]) != root(a_arr[N - 1 - i]):
        ans += 1
        unite(a_arr[i], a_arr[N - 1 - i])

print(ans)
