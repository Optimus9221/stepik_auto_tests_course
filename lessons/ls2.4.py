# Подключил инструменты локаторы и веб драйвер
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
# Объявил функцию
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Объявил переменную браузер
    browser = webdriver.Chrome()
    # Открыл ссылку
    browser.get("https://suninjuly.github.io/execute_script.html")
    # Объявил переменную и положил в нее значение которое нужно для уравнения
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    # Объявил переменную х и положил в нее текст из переменной x_element
    x = x_element.text
    # Объявил переменную y и положил в нее результат вычисления
    y = calc(x)
    # Нашел инпут на странице
    input1 = browser.find_element(By.ID, "answer")
    # Ввел текст в инпут из переменной y
    input1.send_keys(y)
    # Сделал скролл страницы на 100 пикселей
    browser.execute_script("window.scrollBy(0, 100);")
    # Нашел чекбокс на странице и кликнул по нему, чтобы галку поставить
    browser.find_element(By.ID, "robotCheckbox").click()
    # Нашел радиобаттон на странице и кликнул по нему, чтобы галку поставить
    browser.find_element(By.ID, "robotsRule").click()
    # Объявили переменную button и положили в нее кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # Кликнул по кнопке
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Если браузер открыт, закрываем его
    if browser:
        browser.quit()