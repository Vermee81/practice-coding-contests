# https://atcoder.jp/contests/abc064/tasks/abc064_d
from collections import deque
N = int(input())
S = [s for s in input()]
deqS = deque(S)
left = 0
right = 0
for i, s in enumerate(S):
    if s == '(':
        left += 1
    else:
        right += 1

    if right > left:
        deqS.appendleft('(')
        left += 1
        continue

    if i == N - 1 and left > right:
        addStr = ')' * (left - right)
        deqS.append(addStr)
newS = "".join(deqS)
print(newS)
