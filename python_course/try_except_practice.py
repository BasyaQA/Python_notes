def find_average(numbers: list) -> float:
    return sum(numbers) / len(numbers)


print(find_average(numbers=[1, 2, 3, 4, 5]))


# если вместо чисел в листе передать 0, код упадет т.к. деление на 0 невозможно
# что бы код не падал, можно добавить синтаксис для исключений
# try (сделай это)
# except (и если будет это исключение, напиши/выдай то-то)

def find_average(numbers: list) -> float:
    return sum(numbers) / len(numbers)


try:
    find_average(numbers=[])
except ZeroDivisionError:
    print("The list is empty")
