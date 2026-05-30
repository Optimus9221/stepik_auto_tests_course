# Подключил инструменты локаторы и веб драйвер
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
# Подключил инструмент для явных ожиданий
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    # Объявил переменную для браузера
    browser = webdriver.Chrome()
    # Перешел по ссылке из задания
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # Объявил переменную для явного ожидания.
    wait_price = WebDriverWait(browser, 13)
    # Использовал метод для явного ожидания, который ждет появление текста на странице.
    # В данном случае мы нашли элемент с ценой по ID и ждем пока цена не станет равной $100
    wait_price.until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    # Объявил переменную для кнопки
    button = browser.find_element(By.ID, "book")
    # Кликнул по кнопке
    button.click()
    # Нашел число для расчетов
    value1 = browser.find_element(By.ID, "input_value").text
    # Посчитал значение
    value2 = calc(value1)
    # Объявил переменную для поля ввода
    input2 = browser.find_element(By.ID, "answer")
    # Ввел посчитанное значение
    input2.send_keys(value2)
    # Объявил переменную для кнопки
    button2 = browser.find_element(By.ID, "solve")
    # Кликнул по кнопке
    button2.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Если браузер открыт, закрываем его
    if browser:
        browser.quit()