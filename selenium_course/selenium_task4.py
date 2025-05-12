from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker
fake = Faker

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    field_first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    field_first_name.send_keys(Faker().first_name())

    field_last_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    field_last_name.send_keys(Faker().last_name())

    field_email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    field_email.send_keys(Faker().email())

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    welcome_text = welcome_text_elt.text


    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()