# условия

if True:
    print("Hello, world")

x = 10
if x > 0:
    print("x is positive")
else:
    print("x is negative")

# elif условный оператор, когда несколько условий
x = 0
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

# проверка выполнения двух условий
x = 10
y = 20

if x > 0 and y > 0:
    print(x and y)

# ВАЖНО! Когда мы передаем текстовую переменную в условный оператор, всегда будет bool true, если что-то написано в ней

year = 2000

if year % 4 == 0 and year != 0:
    print("Year is leap")
elif year % 400 == 0:
    print("Year is leap")
else:
    print("Year is not leap")
