# https://atcoder.jp/contests/abc199/tasks/abc199_c
N = int(input())
S = list(input())
Q = int(input())

flip_flag = False

for i in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        if flip_flag:
            # aとbのインデックスがNより小さいか比較してN足すのかどうかを決める
            a_idx = a - 1 - N
            if a - 1 < N:
                a_idx = a - 1 + N
            b_idx = b - 1 - N
            if b - 1 < N:
                b_idx = b - 1 + N
            S[a_idx], S[b_idx] = S[b_idx], S[a_idx]
            continue
        S[a - 1], S[b - 1] = S[b - 1], S[a - 1]
        continue
    flip_flag = not flip_flag

if flip_flag:
    newS = "".join(S[N:] + S[:N])
    S = newS

ans = "".join(S)
print(ans)
