# https://atcoder.jp/contests/atc001/tasks/unionfind_a
N, Q = map(int, input().split())
par = [i for i in range(N + 1)]


def root(x: int) -> int:
    if par[x] == x:
        return x
    par[x] = root(par[x])
    return par[x]


def is_same_root(x: int, y: int) -> bool:
    return root(x) == root(y)


def unite(x: int, y: int):
    x = root(x)
    y = root(y)
    if x == y:
        return 0
    par[x] = y


for _ in range(Q):
    p, a, b = map(int, input().split())
    if p == 0:
        unite(a, b)
    else:
        ans = 'Yes' if is_same_root(a, b) else 'No'
        print(ans)

