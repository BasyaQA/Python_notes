# автоматическая загрузка файла
# через поле <input type="file">

# есть такая HTML-форма:
# <input type="file" id="fileUpload">

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("ivan@example.com")

    # создаём временный текстовый файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    with open(file_path, 'w') as file:
        file.write("Hello from Selenium!")

    # загружаем файл
    browser.find_element(By.ID, "file").send_keys(file_path)

    # отправляем форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(10)

finally:
    browser.quit()
