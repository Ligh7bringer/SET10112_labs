from itertools import count, islice
from math import sqrt


def is_prime(n, log=False):
    result = n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))
    if result is True and log:
            print("prime")
    return result


def is_square_sum(part, prime):
    for i in range(1, part):
        if i**2 + i**2 == part:
            print("{}^2 + {}^2 + {}".format(i, i, prime))
            return True
    return False


def is_sum(n):
    for i in range(1, n):
        if is_prime(i):
            part = n - i
            if is_square_sum(part, i):
                return True
    return False


def main():
    num = 5
    while is_prime(num) or is_sum(num):
        num += 2
        print("Checking", num, end=": ")
    print("Outlier!")


main()
