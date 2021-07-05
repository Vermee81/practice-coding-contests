# https://atcoder.jp/contests/abc208/tasks/abc208_b
P = int(input())
fact_list = [1] * 12
for i in range(1, 12):
    fact_list[i] = fact_list[i - 1] * i
j = 10
ans = 0
while P != 0:
    if P >= fact_list[j]:
        P -= fact_list[j]
        ans += 1
    else:
        j -= 1

print(ans)
