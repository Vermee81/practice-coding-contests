p_arr = [[0 for _ in range(550000)] for _ in range(20)]
dep = [0 for _ in range(550000)]


def la(x: int, h: int) -> int:
    for i in range(19, -1, -1):
        if h >= 1 << i:
            x = p_arr[i][x]
            h -= 1 << i
    return x


def lca(u: int, v:int) -> int:
    if dep[u] < dep[v]:
        u, v = v, u
    u = la(u, dep[u] - dep[v])
    if u == v: return u
    for i in range(19, -1, -1):
        if p_arr[i][u] != p_arr[i][v]:
            u = p_arr[i][u]
            v = p_arr[i][v]
    return p_arr[0][v]


if __name__ == '__main__':
    N, Q = list(map(int, input().split()))
    p = list(map(int, input().split()))
    for i in range(1, N):
        p_arr[0][i] = p[i-1]
        dep[i] = dep[p_arr[0][i]] + 1

    for i in range(1, 20):
        for v in range(N):
            p_arr[i][v] = p_arr[i-1][p_arr[i-1][v]]

    for _ in range(Q):
        u, v = list(map(int, input().split()))
        print(lca(u, v))
