# https://atcoder.jp/contests/arc016/tasks/arc016_1
N, M = map(int, input().split())
ok_list = []
for i in range(N):
    if i + 1 != M:
        ok_list.append(i + 1)
print(ok_list[0])
