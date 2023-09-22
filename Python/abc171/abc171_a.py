# https://atcoder.jp/contests/abc171/tasks/abc171_a
S = input()
big_moji = [chr(ord('A') + i) for i in range(26)]
if S in big_moji:
    print('A')
    exit()
print('a')
