def add(x: int, y: int):
    return x + y


print(add(1, 3))


# если нужно сложить множество элементов, используем args (arguments) -> работа с неименованными аргументами
def add_all(*args):
    summary = 0
    for num in args:
        summary += num
    return summary


print(add_all(1, 7, 9, 10))  # tuple

# сложение чисел из двух списков
values = [1, 2, 3, 4, 5]
other_values = [6, 7, 8, 9, 10]

print(add_all(*values, *other_values))


# когда в функцию нужно передать не только числовые аргументы, но и именованные аргументы (ключ-значение)
# используем kwargs

def introduce(**kwargs):  # kwargs - именование аргументы
    print(kwargs)
    print(type(kwargs))


introduce(name="Kate", age=23, city="New York")  # dict


# если хотим, что бы элементы ключ-значение выдавались по отдельности, задаем переменные key, value
def introduce_2(**kwargs):
    for key, value in kwargs.items():  # kwargs - именование аргументы # .items - метод для обращения к элементам
        print(key)
        print(value)


introduce(name="Kate", age=23, city="New York")

# добавить словарь в функцию
person = {
    "city": "Moscow",
    "age": 30
}

introduce_2(**person)
