import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

fake = Faker()

class TestRegistration(unittest.TestCase):

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполняем обязательные поля с использованием уникальных селекторов
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys(fake.first_name())
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys(fake.last_name())
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys(fake.email())

        # Нажимаем кнопку
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Ждём загрузку страницы
        time.sleep(1)

        # Проверка финального текста
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполняем обязательные поля
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys(fake.first_name())
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys(fake.last_name())
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys(fake.email())

        # Нажимаем кнопку
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        time.sleep(1)

        # Проверка текста
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        browser.quit()


if __name__ == "__main__":
    unittest.main()
