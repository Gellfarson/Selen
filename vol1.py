from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_ajax_page():
    # Настройка браузера
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    # Создаем экземпляр драйвера
    driver = webdriver.Chrome(options=options)
    
    try:
        # Переходим на страницу
        driver.get('http://uitestingplayground.com/ajax')
        
        # Ждем и кликаем по синей кнопке
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#ajaxButton'))
        )
        print('Найдена синяя кнопка')
        button.click()
        
        # Ждем зеленой плашки с текстом
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ajaxButton ~ .bg-success'))
        )
        print('Найдена зеленая плашка')
        
        # Получаем и выводим текст
        text = success_message.text.strip()
        print(f'Текст из зеленой плашки: {text}')
        
    except Exception as e:
        print(f'Ошибка при выполнении теста: {str(e)}')
    finally:
        # Закрываем браузер после завершения всех действий
        driver.quit()

# Запускаем тест
test_ajax_page()

