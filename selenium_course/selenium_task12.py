# browser.get("http://example.com") используется для открытия веб-страницы по ссылке

# НЕЯВНЫЕ ОЖИДАНИЯ (implicit wait) -  применяется ко всем find_element
# browser.implicitly_wait(5)

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(5)  # неявное ожидание

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text


# ЯВНЫЕ ОЖИДАНИЯ (explicit wait) - применяется к конкретному случаю — клик, текст, отображение и т.д.
# подожди, пока произойдёт конкретное условие, прежде чем двигаться дальше

# элемент может быть на странице, но невидим (через display: none)
# элемент может быть найден, но не кликабелен (disabled)
# элемент может быть перекрыт другим элементом
# элемент может изменяться в процессе работы скрипта

# ------------------------------
# решение: WebDriverWait + expected_conditions(EC)
# expected_conditions — это готовые функции для использования с WebDriverWait,
# чтобы ждать нужного состояния элемента на странице

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# Ждём до 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.ID, "verify"))
)

button.click()

message = browser.find_element(By.ID, "verify_message")
assert "successful" in message.text

# | Условие                           | Что делает                                   |
# | --------------------------------- | -------------------------------------------- |
# | `presence_of_element_located`     | Элемент существует в DOM                     |
# | `visibility_of_element_located`   | Элемент видим на странице                |
# | `element_to_be_clickable`         | Элемент видим и активен (можно кликнуть) |
# | `text_to_be_present_in_element`   | В элементе есть указанный текст              |
# | `invisibility_of_element_located` | Элемент исчез со страницы                |
# | `alert_is_present`                | Появилось всплывающее окно (alert)           |








