# https://atcoder.jp/contests/abc225/tasks/abc225_d
N, Q = map(int, input().split())

before_list = [i for i in range(N)]
after_list = [i for i in range(N)]

for _ in range(Q):
    q_list = list(map(int, input().split()))
    if q_list[0] == 1:
        x = q_list[1] - 1
        y = q_list[2] - 1
        before_list[y] = x
        after_list[x] = y
        continue
    if q_list[0] == 2:
        x = q_list[1] - 1
        y = q_list[2] - 1
        before_list[y] = y
        after_list[x] = x
        continue
    if q_list[0] == 3:
        start = q_list[1] - 1
        while before_list[start] != start:
            start = before_list[start]

        ans_list = []

        current = start

        while current != after_list[current]:
            ans_list.append(current)
            current = after_list[current]
        ans_list.append(current)

        length = len(ans_list)
        ans_str = " ".join([str(m + 1) for m in ans_list])
        print(length, ans_str)
        continue

