def modify(a):
    print("address of a : ", id(a))
    a = 10
    print("address of a : ", id(a))     # Why address different??
    print("a : ", a)


p = 20
print("address of p : ", id(p))

modify(p)
print("p : ", p)



"""
Python does not have the concept of pass by value/reference. Instead it's all 
about mutable/immutable objects. Hence the moment we try to modify the immutable
object, a new object is created and the value is assigned to this new object 
"""