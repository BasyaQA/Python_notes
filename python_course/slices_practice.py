# считаем элементы с 0
fruits = ["apple", "banana", "cherry", "watermelon"]

print(fruits[0])
print(fruits[-4])

# заменить элементы в списке
fruits[0] = 'pineapple'

# поменять элементы местами в списке
fruits[0], fruits[3] = fruits[3], fruits[0]

# слайсы - выбор ограниченного числа элементов в списке, полуоткрытый интервал (ВАЖНО! элемент с закрывающим индексом не входит в конечную выборку
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[0:3])  # SLICE or new_number=numbers[:len(numbers)]

# слайс с шагом, выведи каждые 2 числа
new_number = numbers[0:10:2]

# индексы можно использовать и для строк
string = "Hello, world"
print(string[5:])
