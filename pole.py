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
    driver.get("http://the-internet.herokuapp.com/inputs")
    
    # Ждем появления поля ввода (максимум 10 секунд)
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='number']"))
    )
    
    # Вводим текст "1000"
    input_field.send_keys("1000")
    print("Введено: 1000")
    time.sleep(1)  # Задержка для визуального подтверждения
    
    # Очищаем поле
    input_field.clear()
    print("Поле очищено")
    time.sleep(1)  # Задержка для визуального подтверждения
    
    # Вводим текст "999"
    input_field.send_keys("999")
    print("Введено: 999")
    time.sleep(1)  # Задержка для визуального подтверждения

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()