# https://atcoder.jp/contests/abc196/tasks/abc196_b
moji = input()
if '.' in moji:
    pos = moji.find('.')
    moji = moji[:pos]
    print(moji)
    exit()
print(moji)
