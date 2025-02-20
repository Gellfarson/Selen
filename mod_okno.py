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
    driver.get("http://the-internet.herokuapp.com/entry_ad")
    
    # Ждем появления кнопки Close (максимум 10 секунд)
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer p"))
    )
    
    # Кликаем по кнопке Close
    close_button.click()
    print("Модальное окно закрыто")
    
    time.sleep(1)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()