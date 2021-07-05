# https://atcoder.jp/contests/atc001/tasks/unionfind_a


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


N, Q = map(int, input().split())
par = [i for i in range(N + 1)]
uf = UnionFind(N + 1)

for _ in range(Q):
    p, a, b = map(int, input().split())
    if p == 0:
        uf.unite(a, b)
    else:
        ans = 'Yes' if uf.is_same_group(a, b) else 'No'
        print(ans)
