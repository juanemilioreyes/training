

def array_sum(list):

    i = 0
    sum = 0

    while i < len(m):
        sum += list[i]
        i += 1
    return sum


def max_num(m):

    max = m[0]
    p = 0
    while p < len(m):
        if max <= m[p]:
            max = m[p]
        p += 1

    return max


def max_num_matrix_mul(m):

    a = 0
    b = 0
    x = 0
    y = 0

    for x in range(0, len(m)):
        for y in range(0, len(m[x])):

            if a <= m[x][y]:
                a = m[x][y]
            if b <= m[x][y] < a:
                b = m[x][y]


    return a*b #returns the maximum number in the maxtrix multiple by the second biggest.

m = [
     [1, 2, 3, 100, 4, 150, 10, 100],
     [1, 2, 3, 100, 40, 1500, 10, 90],
     [1, 2, 3, 103, 4, 150, 10, 89,90,90],
     [1, 2, 3, 1000, 4, 150, 10,75],
     [1, 2, 3, 100, 4, 150, 10,57]
     ]

print max_num_matrix_mul(m)