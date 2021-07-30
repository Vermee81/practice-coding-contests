# https://atcoder.jp/contests/abc211/tasks/abc211_b
from collections import Counter
S1 = input()
S2 = input()
S3 = input()
S4 = input()
count = Counter([S1, S2, S3, S4])
for c in count.values():
    if c != 1:
        print('No')
        exit()
print('Yes')
