# https://atcoder.jp/contests/abc182/tasks/abc182_c
N = input()
num_list = []
for n in N:
    num_list.append(int(n) % 3)
total = sum(num_list)
if total % 3 == 0:
    print(0)
    exit()
if total % 3 == 1:
    if 1 in num_list and len(num_list) > 1:
        print(1)
        exit()
    if 1 in num_list and len(num_list) <= 1:
        print(-1)
        exit()
    if num_list.count(2) >= 2 and len(num_list) > 2:
        print(2)
        exit()
    if num_list.count(2) >= 2 >= len(num_list):
        print(-1)
        exit()
if total % 3 == 2:
    if 2 in num_list and len(num_list) > 1:
        print(1)
        exit()
    if 2 in num_list and len(num_list) <= 1:
        print(-1)
        exit()
    if num_list.count(1) >= 1 and len(num_list) > 2:
        print(2)
        exit()
    if num_list.count(1) >= 1 and len(num_list) <= 2:
        print(-1)
        exit()

print(-1)
exit()







