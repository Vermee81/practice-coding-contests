# https://atcoder.jp/contests/typical90/tasks/typical90_b
N = int(input())

for bit in range((2**N) + 1):
    base_str_arr = ["("] * N
    for i in range(N):
        if bit & 1 << i:
            base_str_arr[N - i - 1] = ")"
    is_valid = True
    left_par_count = 0
    right_par_count = 0
    for l in base_str_arr:
        if l == "(":
            left_par_count += 1
        else:
            right_par_count += 1

        if right_par_count > left_par_count:
            is_valid = False
            break

    if not is_valid:
        continue

    if is_valid and left_par_count == right_par_count:
        ans_str = "".join([str(s) for s in base_str_arr])
        print(ans_str)
