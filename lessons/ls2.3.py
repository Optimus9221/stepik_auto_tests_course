# Подключил инструменты локаторы и веб драйвер
from selenium import webdriver

# Подключил библиотеку для поиска элементов
from selenium.webdriver.common.by import By

# Подключил класс Select — нужен, чтобы работать с выпадающим списком <select> (выбор option по value или тексту)
from selenium.webdriver.support.ui import Select

# Подключил библиотеку time для задержек
import time


try:
    # Объявил переменную link и положил ссылку в неё
    link = "https://suninjuly.github.io/selects1.html"

    # Открыл окно браузера
    browser = webdriver.Chrome()

    # Перешел по ссылке, которая лежит в переменной link
    browser.get(link)

    # Объявил переменную num1 и положил в неё элемент с id num1
    num1 = browser.find_element(By.ID, "num1")

    # Объявил переменную value1 и положил в неё текст элемента num1
    value1= num1.text

    # Объявил переменную num2 и положил в неё элемент с id num2
    num2 = browser.find_element(By.ID, "num2")

    # Объявил переменную value2 и положил в неё текст элемента num2
    value2= num2.text

    # Преобразовал текст чисел в int, сложил и положил сумму в result
    # Текст с страницы ("7") → число 7
    # То же для второго числа
    # Складываем числа, не строки
    # Сохраняем сумму в переменную
    result = int(value1) + int(value2)

    # Нашёл выпадающий список по id dropdown и создал объект Select для выбора пункта
    # browser.find_element(By.ID, "dropdown") — нашли на странице <select id="dropdown">.
    # Select(...) — обернули элемент в класс для работы с выпадающим списком.
    # select = ... — сохранили в переменную, чтобы дальше вызывать методы выбора.
    select = Select(browser.find_element(By.ID, "dropdown"))

    #select_by_visible_text - Выбрать пункт по тексту, который видно в списке
    # str(result) - В списке текст — строка ("10"), не число; PyCharm тоже это ждёт
    select.select_by_visible_text(str(result))

    # Нашёл кнопку отправки формы по классу btn
    button = browser.find_element(By.CSS_SELECTOR, ".btn")

    # Нажал кнопку Submit, чтобы отправить выбранный ответ
    button.click()


finally:
    # Ожидание, чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Если браузер открыт, закрываем его
    if browser:
        browser.quit()