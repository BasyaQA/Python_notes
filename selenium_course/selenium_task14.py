# assert — это встроенная команда Python для проверки утверждений/условий
# Если выражение после assert ложно — выбрасывается исключение AssertionError

# можно добавить сообщение после assert:
# assert abs(-42) == -42, "Should be absolute value of a number"
# abs( ) - это встроенная функция и показывает модуль числа (расстояние от этого значения до 0)

# показывайте ожидаемое и фактическое значения
# assert self.is_element_present('new_announcement_button', timeout=30), "No new announcement button on profile page"

def test_input_text(expected_result, actual_result):
   assert expected_result == actual_result, f"Expected {expected_result}, got {actual_result}"

# 1. Конкатенация (неудобно):
# "Wrong text, got " + actual + ", something wrong"

# 2. str.format():
# "Wrong text, got {}, expected {}".format(actual, expected)

# 3. f-strings (лучше всего):
# f"Wrong text, got {actual}, expected {expected}"


