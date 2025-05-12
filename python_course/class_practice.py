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


# Объект
# Экземпляр класса:
p = Person("Anna")  # p — объект


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
