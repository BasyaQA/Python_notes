# variables scope
def my_function():
    local_var = "I'm local variable"
    print(local_var)  # переменная определена в теле функции!


my_function()

# лучше использовать константы в качестве глобальных переменных (вне скоупа функции)
COMFORTABLE_TEMP = 25


def dif_comfortable_and_temp(temperature: int) -> int:
    return COMFORTABLE_TEMP - temperature


print(dif_comfortable_and_temp(temperature=30))

DEFAULT_LEVEL_EXPERIENCE = 200


def level_up_or_nuh(current_experience: int, new_experience: int) -> bool:
    total_experience = current_experience + new_experience
    if total_experience >= DEFAULT_LEVEL_EXPERIENCE:
        level_up = True
    else:
        level_up = False
    return level_up


player_1 = level_up_or_nuh(current_experience=50, new_experience=30)
print(player_1)
