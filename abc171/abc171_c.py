# https://atcoder.jp/contests/abc171/tasks/abc171_c
N = int(input())

char_list = [chr(ord('a') + i) for i in range(26)]
ans = ""
while N > 0:
    N, a = divmod(N - 1, 26)
    ans = char_list[a] + ans
print(ans)
