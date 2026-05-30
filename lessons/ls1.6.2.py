from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")
print("Кнопка найдена:", button is not None)

input("Нажми Enter, чтобы закрыть браузер...")
browser.quit()
