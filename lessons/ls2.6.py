# Подключил инструменты локаторы и веб драйвер
from selenium import webdriver
from selenium.webdriver.common.by import By
# Импортировал рабочие модули время и математика
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/alert_accept.html")
    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    value1 = browser.find_element(By.ID, "input_value").text
    value2 = calc(value1)
    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(value2)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Если браузер открыт, закрываем его
    if browser:
        browser.quit()