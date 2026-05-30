# Подключил инструменты локаторы и веб драйвер
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
# Объявил функцию
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Объявил переменную link и положил ссылку в неё
    link = "https://suninjuly.github.io/get_attribute.html"
    # Открыл окно браузера
    browser = webdriver.Chrome()
    # Перешел по ссылке, которая лежит в переменной link
    browser.get(link)
    # Объявил переменную x_element и положил в неё элемент с TAG_NAME img
    x_element = browser.find_element(By.TAG_NAME, "img")
    # Объявил переменную x и положил в неё значение атрибута x_element
    x = x_element.get_attribute("valuex")
    # Объявил переменную y и положил в неё результат функции calc(x)
    y = calc(x)
    # Объявил переменную input1 и положил в неё элемент с id answer
    input1 = browser.find_element(By.ID, "answer")
    # Ввёл результат функции calc(x) в поле ввода
    input1.send_keys(y)
    # Объявил переменную option1 и положил в неё элемент с id robotCheckbox
    option1 = browser.find_element(By.ID, "robotCheckbox")
    # Кликнул по элементу option1
    option1.click()
    # Объявил переменную option2 и положил в неё элемент с id robotsRule
    option2 = browser.find_element(By.ID, "robotsRule")
    # Кликнул по элементу option2
    option2.click()
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Если браузер открыт, закрываем его
    if browser:
        browser.quit()