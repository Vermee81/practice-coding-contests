# https://atcoder.jp/contests/abc066/tasks/abc066_b
S = input()
n = len(S)
arr_s = list(S)
while True:
    arr_s = arr_s[:(n-2)]
    n = len(arr_s)
    if arr_s[:(n//2)] == arr_s[(n//2):]:
        print(n)
        exit()
