# https://atcoder.jp/contests/abc200/tasks/abc200_d
N = int(input())
a_arr = list(map(int, input().split()))
# 2**8の中で答えの組み合わせがある。Nが8より小さければ全通り探索する
n = min(N, 8)
# 同じ余りとなる組み合わせのリストを保存するリスト
# ans_judge_list[5] = [1, 2, 5] はa_arr[0]+a_arr[1]+a_arr[4]の余りが5になる
ans_list = [[] for _ in range(200)]
for bit in range(2**n):
    tmp_sum = 0
    tmp_list = []
    for i in range(n):
        if bit & (1 << i):
            tmp_sum += a_arr[i]
            tmp_list.append(i + 1)
    amari = tmp_sum % 200
    if len(ans_list[amari]):
        print('Yes')
        print(len(ans_list[amari]), *ans_list[amari])
        print(len(tmp_list), *tmp_list)
        exit()
    ans_list[amari] = tmp_list

print('No')
