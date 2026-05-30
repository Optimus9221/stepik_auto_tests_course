from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class TestRegistration:

    def test_registration_form(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ищем ТОЛЬКО обязательные поля внутри блока first_block
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Petrov")

        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("ivan.petrov@example.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text

        assert welcome_text == "Congratulations! You have successfully registered!"

        browser.quit()