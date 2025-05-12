# словарь = набор ключ-значение
# ключи словаря всегда уникальны

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(person)

# в словарь, когда он создан, можно присваивать другие ключи
person["job"] = "It guy"
print(person)

# объявляем словарь другим способом
person = {}

person["name"] = "John"
person["age"] = 30
person["city"] = "New York"

# значения в словарях можно вызывать по ключу
print(person["name"])
print(person.get("name"))  # метод/функция get

# если запросить ключ, которого нет, то вернется объект None
# print(person.get["country"])


for item in person.items():
    print(item)
    print(type(item))  # нам распаковывается ключ-значение в виде кортежа

# кортеж можно распаковать в две переменные
for item in person.items():
    key, value = item
    print(item)  # ('name', 'John')
    print(key)  # name
    print(value)  # John
    print(type(item))

# мы можем написать это сразу при объявлении итератора
for key, value in person.items():
    print(key)
    print(value)

# если нужно итерироваться только по ключам/значениям -> keys/values
for key in person.keys():  # у объекта person есть метод keys
    print(key)

# сравнение словарей
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

other_person = {
    "name": "Mary",
    "age": 35,
    "city": "Moscow"

}

print(person == other_person)  # False

# объединить 2 словаря с помощью метода update
other_person_extra_info = {
    "country": "Russia",
    "status": "single",
    "job": "QA"

}

other_person.update(other_person_extra_info)
print(other_person)

# еще один вариант объединения
other_person = other_person | other_person_extra_info
print(other_person)
