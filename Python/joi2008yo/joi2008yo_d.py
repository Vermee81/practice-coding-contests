# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_d
M = int(input())
q_arr = []
for _ in range(M):
    x, y = list(map(int, input().split()))
    q_arr.append((x, y))
N = int(input())
sky_arr = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    sky_arr.append((x, y))
sky_arr = set(sky_arr)

ans = []


def is_all_in(q_arr, sky_arr, move_q_x, move_q_y):
    for q in q_arr:
        if not (q[0] + move_q_x, q[1] + move_q_y) in sky_arr:
            return False
    return True


for q in q_arr:
    for s in sky_arr:
        move_q_x, move_q_y = s[0] - q[0], s[1] - q[1]
        if is_all_in(q_arr, sky_arr, move_q_x, move_q_y):
            ans = [move_q_x, move_q_y]
            break
print(ans[0], ans[1])
