# https://atcoder.jp/contests/abc196/tasks/abc196_c
N = int(input())
counter = 0
for i in range(1, 10**6 + 1):
    if int(str(i) * 2) <= N:
        counter += 1
        continue
    break
print(counter)
