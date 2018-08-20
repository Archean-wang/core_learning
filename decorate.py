#!/usr/bin/env python
#coding:utf-8

from functools import wraps


def log2(param):
    print(param)

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('before log')
            a = func(*args, **kwargs)
            print('after log')
            return a
        return wrapper
    return decorate


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('before log')
        a = func(*args, **kwargs)
        print('after log')
        return a
    return wrapper


@log2('sdf')
def hello():
    print("hello")

if __name__ == "__main__":
    hello()
