class Cylinder:
    pi = 3.14

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2*Cylinder.pi*self.radius*(self.radius + self.height)

    def volume(self):
        return Cylinder.pi*self.radius*self.radius*self.height


cylinder = Cylinder(radius=2, height=3)
print(cylinder.radius)
print(cylinder.height)
print(cylinder.surface_area())
print(cylinder.volume())
