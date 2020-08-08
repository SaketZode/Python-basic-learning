class Animal():
    def __init__(self):
        print("Animal Created...")

    def animal_name(self):
        print("NONE")

    def eat(self):
        print("Animal Eating")

    def make_sound(self):
        print("SOUND")

    def nick_name(self):
        print("nick name")


class Dog(Animal):
    def __init__(self):
        print("Dog Initialized")

    def animal_name(self):
        print("I am Dog")

    def eat(self):
        print("Dog Eating")

    def make_sound(self):
        print("bhow bhow")


class Cat(Animal):
    def __init__(self):
        print("Cat Initialized")

    def animal_name(self):
        print("I am Cat")

    def eat(self):
        print("Cat Eating")

    def make_sound(self):
        print("meow meow")


animal1 = Animal()
animal1.make_sound()
animal = Dog()
animal.animal_name()
animal.eat()
animal.make_sound()
animal.nick_name()
animal = Cat()
animal.make_sound()
animal.nick_name()
