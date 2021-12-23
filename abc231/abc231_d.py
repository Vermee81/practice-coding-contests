# https://atcoder.jp/contests/abc231/tasks/abc231_d
N, M = map(int, input().split())
check_list = [0] * N


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


uf = UnionFind(N)

for _ in range(M):
    a, b = map(int, input().split())
    check_list[a - 1] += 1
    check_list[b - 1] += 1
    if uf.is_same_group(a - 1, b - 1):
        print('No')
        exit()
    uf.unite(a - 1, b - 1)


for c in check_list:
    if c >= 3:
        print('No')
        exit()

print('Yes')
