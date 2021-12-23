# https://atcoder.jp/contests/abc231/tasks/abc231_b
from collections import Counter

N = int(input())
vote = []
for _ in range(N):
    s = input()
    vote.append(s)

vote_counter = Counter(vote)
print(vote_counter.most_common()[0][0])
