a = 10
b = 'asd'

try:
    res = a/b
except ZeroDivisionError:
    print("divide by zero error")
except TypeError:
    print("invalid data types")
except BaseException:
    print("something went wrong")
finally:
    print("bye")
