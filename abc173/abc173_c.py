# https://atcoder.jp/contests/abc173/tasks/abc173_c
H, W, K = map(int, input().split())
masu = [[i for i in input()] for _ in range(H)]
ans = 0

for bit_h in range(2**H):
    for bit_w in range(2**W):
        count = 0
        for i in range(H):
            for j in range(W):
                if not bit_h & (1 << i) \
                        and not bit_w & (1 << j) \
                        and masu[i - 1][j - 1] == '#':
                    count += 1
        if count == K:
            ans += 1

print(ans)
