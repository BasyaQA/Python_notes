from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker
fake = Faker

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.NAME, "firstname")
    for element in elements:
        element.send_keys(Faker().first_name())

    elements = browser.find_elements(By.NAME, "lastname")
    for element in elements:
        element.send_keys(Faker().last_name())

    elements = browser.find_elements(By.NAME, "e-mail")
    for element in elements:
        element.send_keys(Faker().email())

    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys(Faker().word())

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
