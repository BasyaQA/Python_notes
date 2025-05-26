# если мы нашли элемент так:
# element = browser.find_element(By.ID, "treasure")

# то значение атрибута value получаем так:
# x = element.get_attribute("value")  # вернёт строку "123" # always str

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим картинку-сундук
    treasure = browser.find_element(By.ID, "treasure")

    # получаем значение value
    x = treasure.get_attribute("valuex")
    y = calc(x)

    # вводим ответ
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # ставим галочку "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # выбираем радиокнопку "Robots rule!"
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    # жмём кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()






