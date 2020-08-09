class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    """
    For overloading comparison operator (greater than or less than), any one method to be overloaded
    either __gt__ or __lt__. For greater than or equals OR less than or equals, any one from
     __gte__ or __lte__ 
    """
    def __gt__(self, other):
        if self.real == other.real:
            return self.img > other.img
        return self.real > other.real

    """
    For overloading == operator
    """
    def __eq__(self, other):
        return self.real == other.real and self.img == other.img

    """
    For overloading + operator. __sub__ for -, __mul__ for *, __div__ for / 
    and so on......
    """
    def __add__(self, other):
        return (self.real+other.real) + (other.img+other.img)


obj1 = Complex(2, 5)
obj2 = Complex(2, 3)

if obj1 < obj2:
    print("obj2 is greater")
if obj1 > obj2:
    print("obj1 is greater")
if obj1 == obj2:
    print("Equal")


