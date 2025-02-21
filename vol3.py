from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
WebDriverWait(driver, 10).until(lambda driver: len(driver.find_elements(By.TAG_NAME, "img")) >= 3)
images = driver.find_elements(By.TAG_NAME, "img")
src_value = images[2].get_attribute("src")
print(src_value)
driver.quit()