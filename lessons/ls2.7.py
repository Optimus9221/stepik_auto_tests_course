# Подключил инструменты локаторы и веб драйвер
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/redirect_accept.html")
    button = browser.find_element(By.TAG_NAME, "button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    value1 = browser.find_element(By.ID, "input_value").text
    value2 = calc(value1)
    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(value2)
    button2 = browser.find_element(By.TAG_NAME, "button")
    button2.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Если браузер открыт, закрываем его
    if browser:
        browser.quit()