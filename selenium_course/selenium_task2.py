from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker
fake = Faker

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")

    elements = browser.find_elements(By.XPATH, "//input[@name='first_name']")
    for element in elements:
        element.send_keys(Faker().first_name())

    elements = browser.find_elements(By.XPATH, "//input[@name='last_name']")
    for element in elements:
        element.send_keys(Faker().last_name())

    elements = browser.find_elements(By.XPATH, "//input[@class='form-control city']")
    for element in elements:
        element.send_keys(Faker().city())

    elements = browser.find_elements(By.XPATH, "// input[@id = 'country']")
    for element in elements:
        element.send_keys(Faker().country())

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)
