# списки - это структура, которая используется для хранения упорядоченных последовательностей []
fruits = ["apple", "banana", "cherry"]
print(fruits)

# узнать длину списка
print(len(fruits))

# в списке могут быть как строки, так и числовые значения и т.д
# так делать не желательно

my_list1 = [1, 2, 3]
my_list2 = [1, 3, 2]
my_list3 = [1, 2, 3]

print(my_list1 == my_list2)

# узнать, если значение в списке (in - key word)
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

# списки можно задать и так
element1 = "apple"
element2 = "banana"
element3 = "cherry"

fruits = [element1, element2, element3]

# списки можно составлять из строк, вывод ['h', 'e', 'l', 'l', 'o']
word = ("hello")
my_list = list(word)
print(my_list)

# можно складывать списки
my_list4 = my_list1 + my_list2
print(my_list4)

# добавить элемент (метод append()) ! переменная.метод
fruits5 = ["apple", "banana", "cherry"]
fruits.append("watermelon")
print(fruits)

# взять последний элемент списка и присвоить его переменной (метод pop()) ! переменная.метод
fruits = ["apple", "banana", "cherry"]
fruit = fruits.pop()
print(fruit)

# объединить списки (метод extend()) ! переменная.метод
fruits = ["apple", "banana", "cherry"]
fruits2 = ["fig", "grape", "mango"]

fruits.extend(fruits2)
print(fruits)

# вывести элементы списка в обратном порядке (метод reverse()) ! переменная.метод
fruits = ["apple", "banana", "cherry"]
fruit = fruits.reverse()
print(fruit)

# список отсортировать (метод sort()) ! переменная.метод
my_list_list = [1, 3, 4, 5, 12, 15, 555]
my_list_list.sort(reverse=True)  # будет по убыванию, если надо по возрастанию, то оставляем my_list_list.sort()

# создать список из слов из заданной строки (метод split()) ! переменная.метод
new_string = 'My name is Alex'
new_list = new_string.split(" ")
print(new_list)

# собрать из списка строку (метод join()) ! переменная.метод
joined_string = ' '.join(new_list)
print(joined_string)

# узнать самое большое/малое число в списке (метод max/max()), а так же сумму элементов sum ! переменная.метод
my_list_list = [1, 3, 4, 5, 12, 15, 555]
print(max(my_list_list))
print(min(my_list_list))
print(sum(my_list_list))
