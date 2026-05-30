# Подключил инструменты локаторы и веб драйвер
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
first_name = "Иван"
last_name = "Иванов"
email = "ivanov@example.com"

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/file_input.html")
    # Нашел инпут на странице
    input1 = browser.find_element(By.NAME, "firstname")
    # Ввел текст в инпут из переменной first_name
    input1.send_keys(first_name)
    # Нашел инпут на странице
    input2 = browser.find_element(By.NAME, "lastname")
    # Ввел текст в инпут из переменной last_name
    input2.send_keys(last_name)
    # Нашел инпут на странице
    input3 = browser.find_element(By.NAME, "email")
    # Ввел текст в инпут из переменной email
    input3.send_keys(email)
    # Объявил переменную element и положил в неё кнопку с id file
    element = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Если браузер открыт, закрываем его
    if browser:
        browser.quit()