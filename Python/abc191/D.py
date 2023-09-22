from math import floor
X, Y, R = map(float, input().split())
XX = round(X * 10**4)
YY = round(Y * 10**4)
RR = round(R * 10**4)


def inside(x, y):
    return (x-XX)**2 + (y-YY)**2 <= RR**2


def calc_down(x):
    top = floor(Y)
    bottom = top - floor(R)
    if not inside(x, top):
        return 0
    while abs(top - bottom) > 1:
        mid = (top - bottom) // 2
        if inside(x, mid):
            top = mid
            continue
        bottom = mid
    return floor(Y) - bottom


def calc_up(x):
    bottom = floor(Y) + 1
    top = bottom + floor(R)
    if not inside(x, bottom): return 0
    while abs(top - bottom) > 1:
        mid = (top - bottom) // 2
        if inside(x, mid):
            bottom = mid
            continue
        top = mid
    return top - floor(Y) + 1


ans = 0
for i in range(floor(X-R), floor(X+R)+1):
    ans += calc_up(i) + calc_down(i)
print(ans)
