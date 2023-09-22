# https://atcoder.jp/contests/abc213/tasks/abc213_c
H, W, N = map(int, input().split())
x_list, y_list = [], []
for _ in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

x_dict = {x: i + 1 for i, x in enumerate(sorted(list(set(x_list))))}
y_dict = {y: i + 1 for i, y in enumerate(sorted(list(set(y_list))))}

for i in range(N):
    print(x_dict[x_list[i]], y_dict[y_list[i]])

