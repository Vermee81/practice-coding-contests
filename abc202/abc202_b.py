from collections import deque
S = input()
ans_str = deque()
for i, s in enumerate(S):
    if s == "6":
        ans_str.appendleft("9")
        continue
    if s == "9":
        ans_str.appendleft("6")
        continue
    ans_str.appendleft(s)
ans = "".join(ans_str)
print(ans)
