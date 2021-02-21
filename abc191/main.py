from math import floor
from math import ceil
from math import sqrt
if __name__ == '__main__':
    X, Y, R = [0.2, 0.8, 1.1]
    #X, Y, R = [42782.4720, 31949.0192, 99999.99]
    X *= 10**4
    Y *= 10**4
    R *= 10**4
    counter = 0
    for x in range(X-R, X+R+1, 10**4):
        y = round(sqrt(R**2 - x**2))
        if y % (10**4) == 0:
            counter += 1

    lower_X = ceil(X)
    lower_Y = ceil(Y)
    upper_X = ceil(X+R)
    upper_Y = ceil(Y+R)
    counter = 0
    RAN = round(R**2, 4)
    for x in range(int(lower_X), int(upper_X+1)):
        for y in range(int(lower_Y), int(upper_Y+1)):
            if x == X and y == Y:
                counter += 1
                continue
            if x == X and (Y <= y <= Y+R):
                counter += 2
                continue
            if y == Y and (X <= x <= X+R):
                counter += 2
                continue
            k = round((x - X)**2 + (y - Y)**2, 4)
            if k <= RAN:
                counter += 1
                newx = round(X - abs(x-X), 4)
                newy = round(Y - abs(y-Y), 4)
                if round((newx - X)**2 + (y - Y)**2, 4) <= RAN:
                    counter += 1
                if round((newx - X)**2 + (newy - Y)**2, 4) <= RAN:
                    counter += 1
                if round((x - X)**2 + (newy - Y)**2, 4) <= RAN:
                    counter += 1
    print(counter)

