# https://atcoder.jp/contests/abc197/tasks/abc197_c
N = int(input())
a_arr = list(map(int, input().split()))
ans = 2**30
for bit in range(2**(N - 1)):
    h_or = a_arr[0]
    h_xor = 0
    for i in range(1, N):
        if bit & 1 << (i - 1):
            h_xor ^= h_or
            h_or = 0
        h_or |= a_arr[i]
    h_xor ^= h_or
    ans = min(ans, h_xor)
print(ans)
