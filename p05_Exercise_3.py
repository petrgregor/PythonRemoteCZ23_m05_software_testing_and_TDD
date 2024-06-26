""" Exercise 3

Write the func function that satisfies this test.
"""


def func(number):
    return int(str(number)[0::2]) * 2


if __name__ == '__main__':
    print(func(123))
