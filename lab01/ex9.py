from itertools import count, islice
from math import sqrt


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))


def calc_num(num):
    result = num*num - num + 41
    ret = is_prime(result)
    if ret is False:
        print("{} is not prime!".format(result))
    return ret


def start():
    num = 0
    while True:
        if calc_num(num) is False:
            print("{} is the first occurrence!".format(num))
            break
        num += 1


start()

