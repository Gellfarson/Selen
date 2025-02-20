from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


firefox_options = Options()

driver = webdriver.Firefox(options=firefox_options)

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/login")
    
    # Ждем появления поля username (максимум 10 секунд)
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    
    # Вводим "tomsmith" в поле username
    username_field.send_keys("tomsmith")
    print("Введён username: tomsmith")
    
    # Находим поле password
    password_field = driver.find_element(By.ID, "password")
    
    # Вводим "SuperSecretPassword!" в поле password
    password_field.send_keys("SuperSecretPassword!")
    print("Введён password: SuperSecretPassword!")
    
    # Ждем, пока кнопка Login станет кликабельной
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    
    login_button.click()
    print("Нажата кнопка Login")
    
    time.sleep(2)
    
    # Проверяем, что авторизация прошла успешно
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "flash"))
    )
    if "You logged into a secure area!" in success_message.text:
        print("Авторизация успешна!")
    else:
        print("Ошибка авторизации")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()