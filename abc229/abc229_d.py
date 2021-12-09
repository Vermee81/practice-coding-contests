# https://atcoder.jp/contests/abc229/tasks/abc229_d
S = input()
K = int(input())
ans = 0
tail_idx = 0

cum_dot = [0] * (len(S) + 1)

for i in range(len(S)):
    if S[i] == '.':
        cum_dot[i + 1] = cum_dot[i] + 1
    else:
        cum_dot[i + 1] = cum_dot[i]


def can_swap_to_x(start: int, end: int) -> bool:
    if cum_dot[end] - cum_dot[start] > K:
        return False
    return True


for head_idx in range(len(S)):
    while tail_idx <= len(S) - 1 and can_swap_to_x(head_idx, tail_idx + 1):
        tail_idx += 1
    ans = max(ans, tail_idx - head_idx)

print(ans)
