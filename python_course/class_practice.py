# Класс
# Шаблон для создания объектов:
class Person:
    pass


# Конструктор класса
# Метод, который запускается при создании объекта:
class Person:
    def __init__(self, name):
        self.name = name


# Методы класса
# Функции внутри класса:
class Person:
    def greet(self):
        print("Hello")


# Объект/Инстанс/Экземпляр
# Экземпляр класса:
p = Person  # p — объект
Person = "Anna"


# Что возвращает функция
# return возвращает результат:
def sum(a, b):
    return a + b


x = sum(2, 3)  # x = 5


# self
# Ссылка на текущий объект в методах класса:
class Person:
    def say_name(self):
        print(self.name)


# init
# Специальный метод-конструктор класса:
def __init__(self, name):
    self.name = name


# try, exception, finally
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Error!")
finally:
    print("This always runs")


# создание класса MyClass
class MyClass:
    pass


print(type(MyClass))  # type

# экземпляр класса MyClass
my_class = MyClass()
print(type(my_class))


# метод инициализации класса (дандер-метод "магические методы" т.е. в синтаксисе 2 нижних подчеркивания, спереди и сзади)
# дандер-методы определяют как будет вести себя объект класса с разными конструкциями языка

class Ork:  # задаем класс
    def __init__(self, level: int) -> None:  # __init__ функция работает при создании экземпляра конкретного класса
        self.level = level  # то же самое что ork.level
        self.health_points = 100 * level
        self.attack_power = 100 * level

    def attack(self):
        print(f"Ork attacks with {self.attack_power} power")

    def __str__(self):
        return f"Ork (level: {self.level}, hp: {self.health_points}"


ork = Ork(level=1)  # задаем экземпляр класса
print(ork.level)  # атрибут level
print(ork.health_points)
print(ork.attack_power)

ork.attack()
print(ork)

# Атрибуты - это данные объекта,
# в то время как методы - это функции, которые совершают операции над этими данными

# __innit__ используем для создания экземпляра класса
# self - экземпляр класса

# __str__ задает то, что пользователь увидит при вызове функции print()

# наследование у классов
# создадим еще одного героя с практически идентичным кодом


class Elf:
    def __init__(self, level: int) -> None:  # __init__ функция работает при создании экземпляра конкретного класса
        self.level = level  # то же самое что ork.level
        self.health_points = 50 * level
        self.attack_power = 15 * level

    def attack(self):
        print(f"Elf attacks with {self.attack_power} power")

    def __str__(self):
        return f"Elf (level: {self.level}, hp: {self.health_points}"
