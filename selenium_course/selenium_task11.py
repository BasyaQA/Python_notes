# browser.window_handles — список всех открытых вкладок(в
# browser.switch_to.window(handle) — переключиться на вкладку по её handle
# browser.current_window_handle — получить handle текущей вкладки

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # нажимаем кнопку, которая открывает новую вкладку
    browser.find_element(By.TAG_NAME, "button").click()

    # сохраняем имя текущего окна
    original_window = browser.window_handles[0]

    # ждём, пока новая вкладка появится (второе окно)
    new_window = browser.window_handles[1]

    # переключаемся на новую вкладку
    browser.switch_to.window(new_window)

    # далее работаем с новой страницей
    x = browser.find_element(By.ID, "input_value").text
    answer = str(math.log(abs(12 * math.sin(int(x)))))
    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.TAG_NAME, "button").click()

    # получаем ответ из alert
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()



