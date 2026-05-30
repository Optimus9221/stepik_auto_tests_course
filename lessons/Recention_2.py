from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")

    input1 = browser.find_element(
        By.CSS_SELECTOR,
        ".first_block .first_class .form-control"
    )
    input1.send_keys("Ivan")

    input2 = browser.find_element(
        By.CSS_SELECTOR,
        ".first_block .second_class .form-control"
    )
    input2.send_keys("Petrov")

    input3 = browser.find_element(
        By.CSS_SELECTOR,
        ".first_block .third_class .form-control"
    )
    input3.send_keys("test@test.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()