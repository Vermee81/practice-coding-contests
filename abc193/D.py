# https://atcoder.jp/contests/abc193/tasks/abc193_d
K = int(input())
S = input()[:4]
S = [int(i) for i in S]
T = input()[:4]
T = [int(i) for i in T]
score_s_now = 0
score_t_now = 0
nokori = [K] * 10
for c in S:
    nokori[c] -= 1
for c in T:
    nokori[c] -= 1


def score(cards: list) -> int:
    score = 0
    for i in range(1, 10):
        s_num = cards.count(i)
        score += i * (10 ** s_num)
    return score


counter = 0

for i in range(1, 10):
    if nokori[i] == 0:
        continue
    for j in range(1, 10):
        if nokori[j] == 0 or i == j:
            continue
        new_s = S[:]
        new_t = T[:]
        new_s.append(i)
        new_t.append(j)
        score_s = score(new_s)
        score_t = score(new_t)
        if score_s > score_t:
            counter += nokori[i] * nokori[j]
for i in range(1, 10):
    if nokori[i] < 2:
        continue
    new_s = S[:]
    new_t = T[:]
    new_s.append(i)
    new_t.append(i)
    score_s = score(new_s)
    score_t = score(new_t)
    if score_s > score_t:
        counter += nokori[i] * (nokori[i] - 1)

all_pattern = 9 * K - 8
print(counter / all_pattern / (all_pattern - 1))
