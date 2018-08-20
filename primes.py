#!/usr/bin/env python3
# coding:utf-8


def natural():
    i = 2
    while True:
        yield i
        i += 1


def _division(n):
    return lambda x: x % n


def prime():
    num = natural()
    while True:
        n = next(num)
        yield n
        num = filter(_division(n), num)
        #切记不能写成num = filter(lambda x: x % n, num)
        #因为生成器是惰性的，执行时n已经是最后一个数，所以要用到闭包_division

if __name__ == "__main__":
    for i in prime():
        if i < 200:
            print(i)
        else:
            break