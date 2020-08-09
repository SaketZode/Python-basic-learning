import sys as s

s.setrecursionlimit(2000)       # set recursion limit (1000 by default)
print(s.getrecursionlimit())    # fetch recursion limit


def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


res = fact(6)
print(res)
