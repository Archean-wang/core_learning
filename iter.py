# !/usr/bin/env python
# coding:utf-8


class Fib:
    def __init__(self):
        self.pre = 0
        self.cur = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.pre, self.cur = self.cur, self.pre + self.cur
        return self.cur


def Fib2(num):
    count, pre, cur = 1, 0, 1
    yield 1
    while count <= num-1:
        count += 1
        pre, cur = cur, pre + cur
        yield cur


# a = Fib()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
if __name__ == "__main__":
    print(list(Fib2(7)))
