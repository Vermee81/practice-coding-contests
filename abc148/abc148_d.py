# https://atcoder.jp/contests/abc148/tasks/abc148_d
N = int(input())
a_arr = list(map(int, input().split()))
seikai_list = [i for i in range(1, N + 1)]
counter = 0
seikai_idx = 0
for a in a_arr:
    seikai = seikai_list[seikai_idx]
    if a == seikai:
        seikai_idx += 1
        continue
    counter += 1

if seikai_idx == 0:
    print(-1)
    exit()

print(counter)
