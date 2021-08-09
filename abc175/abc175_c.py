# https://atcoder.jp/contests/abc175/tasks/abc175_c
X, K, D = map(int, input().split())

if K * D <= abs(X):
    print(abs(X) - (K * D))
    exit()

koeru_dist = abs((abs(X) // D + 1) * D - abs(X))
koenai_dist = abs(X) % D
nokori = 0
if koenai_dist > koeru_dist:
    nokori = K - (abs(X) // D + 1)
    if nokori % 2 == 0:
        print(koeru_dist)
        exit()
    else:
        print(koenai_dist)
        exit()

if koenai_dist <= koeru_dist:
    nokori = K - (abs(X) // D)
    if nokori % 2 == 0:
        print(koenai_dist)
        exit()
    else:
        print(koeru_dist)
        exit()


