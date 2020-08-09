a = 10
print("id of a during assignment : ", id(a))    # value 10 assigned to object a


def modify():
    global a    # accessing reference of global a
    print("id of a initially in modify() function : ", id(a))
    a = 15
    """
    integer being immutable older (global) object is deleted 
    and a now holds reference of newly created object
    """
    print("id of a after modifying the value : ", id(a))
    print("value of a inside : ", a)


modify()

print("value of a outside : ", a)


# using globals() function


p = 20
print("id of p : ", id(p))


def update():
    x = globals()['p']    # a local variable x is created which points to global object p
    print("id of x : ", id(x))
    x = 25
    """
    int being immutable, new object is created and x points 
    to this new object leaving value of object p unchanged
    """
    print("id of x after updating value : ", id(x))
    print("inside x : ", x)


update()

print("value of p outside : ", p)


# swapping two numbers

x = 10
y = 20


def swap():
    global x
    global y
    x, y = y, x
    print("inside swap function : {} {}".format(x, y))


swap()

print("outside swap function : {} {}".format(x, y))
