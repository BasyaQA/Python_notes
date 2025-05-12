# более удобный способ создания списков

squares = []
for x in range(10):
    squares.append(x ** 2)  # append = add new element to list

print(squares)

even_squares = []
for x in range(10):
    if x % 2 == 0:  # если делится без остатка на 2
        even_squares.append(x ** 2)

print(even_squares)

# есть cписок чисел: каждое четное заменим словом even, а нечетное словом odd

labelled_numbers = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        labelled_numbers.append("even")
    else:
        labelled_numbers.append("odd")

print(labelled_numbers)
