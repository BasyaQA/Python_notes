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

from datetime import date


class Animal:
    def __init__(self, name: str, birthday: date, pipi_size: int):
        self.name = name
        self.birthday = birthday
        self.pipi_size = pipi_size

    def days_till_bday(self):
        pass


class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof! My pipi size is {self.pipi_size}"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow! My pipi size is {self.pipi_size}"


animals = Dog("Buddy", date(2012, 2, 3), 10), Cat("Whiskers", date(2018, 12, 3), 12)

for animal in animals:
    print(animal.speak())
    animal.days_till_bday()

# def print_hello(name: str) -> None:
#     print(f"Hello, {name}!")
#
#
# print_hello("Nastya")
