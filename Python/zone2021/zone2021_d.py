# https://atcoder.jp/contests/zone2021/tasks/zone2021_d
from collections import deque

S = input()
flip_flag = False
T = deque()

for s in S:
    # フラグを反転させるだけ
    if s == 'R':
        flip_flag = not flip_flag
        continue
    # 長さ0なら最後に追加する
    if len(T) == 0:
        T.append(s)
        continue
    # 反転した状態で操作する
    if flip_flag:
        # 付け足すことで同じ文字が連続しそうなら削除する
        if T[0] == s:
            T.popleft()
        else:
            T.appendleft(s)
    # 反転してない状態で操作する
    else:
        # 付け足すことで同じ文字が連続しそうなら削除する
        if T[-1] == s:
            T.pop()
        else:
            T.append(s)

# 最後に反転した状態なら反転させる
if flip_flag:
    T.reverse()
print("".join(T))
