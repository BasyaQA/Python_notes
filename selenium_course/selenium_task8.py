# МЕТОД execute_script

# показать всплывающее окно (alert):
# browser.execute_script("alert('Привет!');")

# изменить заголовок вкладки:
# browser.execute_script("document.title='Новый заголовок';")

# прокрутить страницу к элементу:
# иногда элемент перекрыт футером. Тогда делаем:

# button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()



# Можно протестировать скрипт сначала в консоли браузера (F12 → Console), и потом — в автотесте

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считываем x и считаем функцию
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # вводим ответ в поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # скроллим вниз до кнопки
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # отмечаем чекбокс и радиокнопку
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()
