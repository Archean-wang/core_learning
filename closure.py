# ！/usr/bin/env python
# coding:utf-8


def counter(num):
    count = [num]

    def inc():
        count[0] += 1
        return count[0]

    return inc


if __name__ == "__main__":
    count1 = counter(1)
    print(count1())
    print(count1())
