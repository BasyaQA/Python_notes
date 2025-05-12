# функции бывают встроенные, а бывают созданные нами (функция - блок кода для многократного повторения)

numbers_1 = [1, 2, 3, 4, 5]

average_num_1 = sum(numbers_1) / len(numbers_1)  # сумма элементов / на длину этого списка
print(average_num_1)

# dry (don't repeat yourself) = поэтому если среднее значение нужно для нескольких списков, делаем функцию

numbers_2 = [6, 7, 8, 9, 10]


def find_average(numbers):  # определяем аргумент (последовательность) numbers и обязательно нужно ключевое слово def
    average = sum(numbers) / len(numbers)
    return average  # и ключевое слово return что бы выводился результат вычислений внутри функции


average_2 = find_average(numbers_2)
print(average_2)


# зададим переменную по подсчету гласных

def count_vowels(string):
    VOWELS = "aeiouAEIOU"  # константа - не переменное значение, всегд а капсом
    count = 0  # переменная для подсчета гласных
    for char in string:
        if char in VOWELS:
            count += 1

    return count


print(count_vowels("Hello world"))


# функция - заглушка, ничего не делает

def nothing():
    print("This function does nothing")
    pass  # ключевое слово pass


def format_date(date: int, month: str) -> str:  # можно ставить * и мы будем вынуждены описывать переменные
    return f"The date is {date} of {month}"  # и можно указать тип возвращаемого значения: -> str


print(format_date(15, "May"))


# в функции можно объявлять дефолтные аргументы
def custom_greeting(*, name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


print(custom_greeting(name="Judy"))
