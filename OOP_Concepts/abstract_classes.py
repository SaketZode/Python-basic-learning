"""
ABC stands for Abstract Base Class.
Python by default does not support abstract classes.
To implement the concept like interfaces in java or abstract classes in cpp,the base class must inherit ABC from abc.
The decorator (just like annotations in java) has to be added to make method as abstract.
Keyword pass must be used in the definition part of the method.
The inheriting classes must implement the methods declared in base class else will throw compiler error.
Base class cannot be instantiated
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Cat(Animal):
    def make_sound(self):
        print("meow meow")

    def eat(self):
        print("cat eating...")

    def sleep(self):
        print("cat sleeping...")


class Dog(Animal):
    def make_sound(self):
        print("bhow bhow")

    def eat(self):
        print("dog eating...")

    def sleep(self):
        print("dog sleeping")


animal = Dog()
animal.make_sound()

animal = Cat()
animal.make_sound()