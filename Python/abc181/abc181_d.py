# https://atcoder.jp/contests/abc181/tasks/abc181_d
from collections import Counter
S = input()
s_counter = Counter([s for s in S])

if len(S) <= 2:
    if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
        print('Yes')
        exit()
    print('No')
    exit()

three_digits_eight = [str(i) for i in range(104, 1000, 8)]
three_digits_eight.append('000')

ok_flag = False
for tde in three_digits_eight:
    td_counter = Counter(tde)
    warikireru = True
    for k in td_counter.keys():
        if s_counter[k] < td_counter[k]:
            warikireru = False
            break
    if warikireru:
        ok_flag = True

if ok_flag:
    print('Yes')
    exit()
print('No')
