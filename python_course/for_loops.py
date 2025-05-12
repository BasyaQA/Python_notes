# вывести каждый элемент списка
file_names = ['document.doc', 'document_2.doc']

for file in file_names:
    print(file)

# вывести каждый элемент строки
string = "Hello darkness my old friend"
for char in string:  # char  - символ
    print(char)

# посчитать количество букв "о"
string = "Hello darkness my old friend"
count_o = 0
for char in string:  # char  - символ
    if char == "o":
        count_o += 1  # syntaxis sugar: count_o = count_o + 1
        print(char)
print(count_o)

# двухуровневый цикл (на первом цикле вывели имя, затем вывели имя по буквам
students = ["Maria", "Jane", "Liza"]

for student in students:
    print(student)
    for char in student:
        print(char)

# CONTINUE, BREAK - ключевые слова
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for num in numbers:
    if num % 2 == 0:  # если делится без остатка на 2, то пропусти и продолжи итерацию
        continue
    print(num)

for num in numbers:
    if num == 10:
        break  # если число = 10, останови итерацию

    print(num)

# range() - функция, которая генерирует последовательности чисел
range_object = range(10)  # range(1, 10) or range(1,10,2) - каждое второе число в последовательности
print(range_object)

# переводим последовательность из функции в список
numbers = list(range_object)
print(numbers)

# последовательность может быть на убывание
my_range = range(10, 1, -1)  # шаг -1
print(list(my_range))

# прибавить +1 к каждому числу в списке можно только изменив его индекс
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in range(len(numbers)):  # i - переменная "индекс"
    numbers[i] += 1

print(numbers)

# определить количество букв "о" в строке и их индекс
greeting = "Hello darkness my old friend"

indexes = []
count = 0

for i in range(len(greeting)):
    if greeting[i] == "o":
        count += 1
        indexes.append(i)

print(indexes, count)
