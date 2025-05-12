# коллекция из уникальных неупорядоченных элементов

my_set = {1, 2, 3, 4, 5}
print(type(my_set))  # set

my_set = set()
for i in range(5):
    my_set.add(i)  # add method or remove
my_set.remove(2)

print(my_set)

# set содержит уникальные значения, без дублей
my_set = {1, 2, 3, 4, 5}
my_set_2 = {2, 3, 4, 5, 12, 13}

united_set = my_set.union(my_set_2)
print(united_set)

# найти пересечение/отличие в сетах -> intersection/difference
print(my_set.intersection(my_set_2))

# еще один вариант написания кода для выявления уникальных данных и внесения их в сет
numbers = [1, 2, 3, 455, 4, 5, 55, 5, 7, 7]

unique_num = list(set(numbers))
print(unique_num)
print(type(unique_num))  # list
