# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_e
R, C = list(map(int, input().split()))
senbei_pos = []
ans = 0
for _ in range(R):
    pos = list(map(int, input().split()))
    senbei_pos.append(pos)

for bit in range(2**R):
    total = 0
    copied_pos = senbei_pos[:]
    # Rの上限が10なので10桁の2進数になるように0で埋める
    flip_row_pos = list(format(bit, '010b'))
    for j in range(C):
        column = [p[j] for p in copied_pos]
        one_count = sum([column[k] ^ int(flip_row_pos[10 - R + k])
                         for k in range(R)])
        zero_count = R - one_count
        total += max(zero_count, one_count)
    ans = max(ans, total)
print(ans)
