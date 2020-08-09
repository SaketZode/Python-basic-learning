class A:
    def __init__(self):
        print("Class A init method")

    def feature1(self):
        print("A-1 feature")

    def feature2(self):
        print("A-2 feature")


class B(A):
    def __init__(self):
        super().__init__()
        print("Class B init method")

    def feature3(self):
        print("B-3 feature")

    def feature4(self):
        print("B-4 feature")


obj = B()

# all features of class A inherited to class B

obj.feature1()
obj.feature2()
obj.feature3()
obj.feature4()

"""
If child class has no init method defined, then it will look in parent 
class for init method and execute it if present in parent class.

if init method is defined in child class, then it will execute child's init 
method and no parent class' init method will be executed if object is of child 
class' type
-> In this case, parent's init method can be called using super() method
"""

# Ambiguous function case


class C:
    def __init__(self):
        print("Class C init method")

    def feature1(self):
        print("C-1 feature")

    def feature2(self):
        print("C-2 feature")


class D:
    def __init__(self):
        print("Class D init method")

    def feature2(self):
        print("D-1 feature")

    def feature4(self):
        print("D-4 feature")


class E(C, D):
    def __init__(self):
        print("Class E init method")


obj = E()
obj.feature2()

"""
In case of ambiguous function calls, it follows left-to right order in case
of multiple inheritance. Example, C is in left side on line 68 and D on the
right side. Hence, function defined in class C will be called.
"""

