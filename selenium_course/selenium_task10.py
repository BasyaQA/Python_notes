# виды alert:

# alert - ок (alert.accept())

#confirm - ок or dismiss (cancel)
# confirm.accept()
# confirm.dismiss()

# prompt - ввести текст, or or dismiss
# prompt.accept()
# prompt.dismiss()
# prompt.send_keys()

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # нажимаем на кнопку, которая вызывает confirm
    browser.find_element(By.TAG_NAME, "button").click()

    # принимаем confirm
    browser.switch_to.alert.accept()

    # считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer = calc(x)

    # вводим ответ
    browser.find_element(By.ID, "answer").send_keys(answer)

    # нажимаем Submit
    browser.find_element(By.TAG_NAME, "button").click()

    # получаем результат из алерта
    alert = browser.switch_to.alert
    print(alert.text)

    # примем алерт
    alert.accept()

finally:
    time.sleep(10)
    browser.quit()


