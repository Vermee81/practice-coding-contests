# https://atcoder.jp/contests/abc075/tasks/abc075_c


class UnionFind:
    def __init__(self, n: int):
        self.parents = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def root(self, x: int) -> int:
        if self.parents[x] == x:
            return x
        self.parents[x] = self.root(self.parents[x])
        return self.parents[x]

    def is_same_group(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def get_group_size(self, x: int) -> int:
        return self.size[self.root(x)]

    def unite(self, x: int, y: int):
        gx = self.root(x)
        gy = self.root(y)
        if gx == gy:
            return 0
        if self.size[gx] < self.size[gy]:
            self.parents[gx] = gy
            self.size[gy] += self.size[gx]
        else:
            self.parents[gy] = gx
            self.size[gx] += self.size[gy]


N, M = map(int, input().split())
ab_list = [list(map(int, input().split())) for _ in range(M)]

ans = 0
for h in range(M):
    uf = UnionFind(N)
    alone = False
    for h2 in range(M):
        if h == h2:
            continue
        uf.unite(ab_list[h2][0] - 1, ab_list[h2][1] - 1)

    for n in range(N):
        size = uf.get_group_size(n)
        if size != N:
            alone = True

    if alone:
        ans += 1
print(ans)


