import math


def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    m = 3
    if n % m == 0:
       return False
    else:
        while m <= math.sqrt(n):
            m += 1
            if n % m == 0:
                return False

        return True


if is_prime(20000):
    print "Is Prime"
else:
    print "Is Not Prime"
