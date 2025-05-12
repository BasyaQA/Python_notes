from python_course.variables_types import my_integer

my_string = "Hello world"

# """ ... """ внутрь можно поместить большой многострочный текст

# сложение строк

first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)

# len() - узнать длину строки
length = len(full_name)
print(length)

# str - ключевое слово для перевода в строку любого другого типа данных
my_integer = 100
my_string = str(my_integer)
print(my_string)

# просим число, будет числовой формат вместо текста
my_string = int(input("Enter a number:"))
print(type(my_string))

# посчитаем количество цифр в большом числе (str!!!) считает в формате строки, не числа
big_integer = 2 ** 1000
print(len(str(big_integer)))

# входит ли слово в строку (true/false)
my_string = "Hello, world"
print("Hello" in my_string)

# написать строку КАПСОМ (метод upper()) ! переменная.метод
my_string = "Hello, world"
print(my_string.upper())

# написать строку малым регистром (метод lower()) ! переменная.метод
my_string = "Hello, world"
print(my_string.lower())

# убрать лишние пробелы справа и слева (метод strip()) ! переменная.метод
my_string = "Hello, world"
print(my_string.strip())

# заменить слово или символы внутри строки (метод replace()) ! переменная.метод
my_string = "Hello, world"
print(my_string.replace("world", "python"))

# определить количество символов (метод count()) ! переменная.метод
my_string = "Hello, world"
print(my_string.count("rl"))

# определить: в строке цифры или буквы, НЕ ТИП ДАННЫХ - РАБОТА СО СТРОКОЙ (метод isdigit()) ! переменная.метод
my_string = "10"
print(my_string.isdigit())

# если в строке число, то переведи его в тип данных - числовой
integer = input("Enter a number:")
if integer.isdigit():
    integer = int(integer)
else:
    print(f"{my_string}) is not a number")

print(type(integer))

# вставить данные в строку (форматирование) f-строка {}
name = Alice
age = 25
print(f"My name is {name} and my age is {age}")
