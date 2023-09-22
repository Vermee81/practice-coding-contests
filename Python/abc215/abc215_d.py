# https://atcoder.jp/contests/abc215/tasks/abc215_d
N, M = map(int, input().split())
a_arr = list(map(int, input().split()))


def prime_factorization(n: int) -> list:
    prime_list = []
    if n == 1:
        return [1]
    for i in range(2, int(n ** 0.5) + 1):
        while True:
            if n % i == 0:
                prime_list.append(i)
                n //= i
                continue
            break

    if n > int(n ** 0.5):
        prime_list.append(n)

    return prime_list


prime_set = set()

for a in a_arr:
    if a == 1:
        continue

    prime_a_list = prime_factorization(a)

    for p in prime_a_list:
        prime_set.add(p)


ans_judge_list = [True] * (M + 1)

for p in prime_set:
    k = 1
    while p * k <= M:
        ans_judge_list[p * k] = False
        k += 1

ans_list = []
for i in range(1, M + 1):
    if ans_judge_list[i]:
        ans_list.append(i)

print(len(ans_list))
ans_list.sort()
for ar in ans_list:
    print(ar)
