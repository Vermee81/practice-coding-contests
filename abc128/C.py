# https://atcoder.jp/contests/abc128/tasks/abc128_c
N, M = list(map(int, input().split()))
s_arr = []
count = 0
for _ in range(M):
    kss = list(map(int, input().split()))
    s_arr.append(kss[1:])
p = list(map(int, input().split()))
for bit in range(1 << N):
    all_bright = True
    for i, s in enumerate(s_arr):
        c = 0
        for ss in s:
            if bit & (1 << (ss-1)):
                c += 1
        if c % 2 != p[i]:
            all_bright = False
            break
    if all_bright:
        count += 1
print(count)
