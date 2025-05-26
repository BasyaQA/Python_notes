# class Dog:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def bark(self):
#         return f"{self.name} says woof!" # f-строка (или форматированная строка)
#
# my_dog=Dog("Buddy", 6)
# print(my_dog.age)
# print(my_dog.bark())


# Вместо переменной класса age у нас birthday
# Мы передаем на вход дату рождения животного; получаем текущую дату
# Нам нужно вывести кол-во дней до дня рождения, а если др сегодня, то вывести С днем рождения

# from datetime import date
#
# class Animal:
#     def __init__(self, name: str, birthday: date):
#         self.name = name
#         self.birthday = birthday
#
#     def days_till_bday(self):
#         pass


# Вам необходимо разработать программу
# для расчёта площади различных геометрических фигур, таких как круги, прямоугольники и треугольники.
#
# Создайте:
#
# класс Shape, который будет базовым классом для всех фигур
# и будет хранить пустой метод area,
# который наследники должны переопределить;

# класс Circle;
# класс Rectangle;
# класс Triangle.

# Классы Circle, Rectangle и Triangle наследуют от класса Shape и реализуют метод для вычисления площади фигуры.
#
# На основе этой информации сделайте так, чтобы:
#
# Нельзя было создавать объекты класса Shape.
# Наследники класса Shape переопределяли его метод area, чтобы объекты этих классов можно было использовать.
#
# Shape для него надо использовать absract class, остальные классы должны наследоваться от этого

from math import sqrt, pi
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def __init__(self, name: str):
        self._name = name

    def print_name(self):
        print(self._name)


class Circle(Shape):
    def __init__(self, radius, name):
        super().__init__(name)
        self.radius = radius

    def area(self):
        circle_shape = pi * self.radius ** 2
        print(circle_shape)


circle_1 = Circle(radius=5, name="Shape Circle")
circle_1.area()
print(circle_1.radius)
circle_1.print_name()


class Triangle(Shape):
    def __init__(self, a, b, c, name):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        triangle_shape = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        print(triangle_shape)

rectangle_1 = Triangle(a=5, b=5, c=5, name="Shape Triangle")
rectangle_1.area()
rectangle_1.print_name()


class Rectangle(Shape):
    def __init__(self, a, b, name):
        super().__init__(name)
        self.a = a
        self.b = b

    def area(self):
        rectangle_shape = self.a * self.b
        print(rectangle_shape)

rectangle_1 = Rectangle(a=5, b=15, name="Shape Rectangle")
rectangle_1.area()
rectangle_1.print_name()


