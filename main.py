from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
driver = webdriver.Chrome()
# driver.maximize_window()  # Maximize window

try:
    # Go to website
    driver.get("http://localhost:8080")
    
    # Wait for search box to be visible (explicit wait)
    wait = WebDriverWait(driver, 20)

    user_input = wait.until(
        EC.presence_of_element_located((By.NAME, "j_username"))
    )
    user_input.send_keys(Keys.RETURN)

    all_menu_items = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "gs-application-list-item__title"))
    ) 
    # Ищем элемент по тексту и кликаем на него
    target_text = "Настройка системы"  # замените на нужный текст
    found = False
    
    for item in all_menu_items:
        print(item.text)
        if item.text.strip() == target_text:
            print(f"Найден элемент с текстом: {target_text}")
            item.click()
            found = True
            break
    
    if not found:
        print(f"Элемент с текстом '{target_text}' не найден")

    time.sleep(2)
    
    element = wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, "input"))
    )
    element.send_keys(Keys.LEFT_CONTROL + Keys.ALT + Keys.SHIFT + "e")
    
    time.sleep(2)

    gid_field = wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, "input"))
    )
    gid_field.click()
    gid_field.send_keys("16151/141260")
    gid_field.click()
    driver.implicitly_wait(5)
    gid_field.send_keys(Keys.ENTER)
    
    
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Keep browser open for a while
    input("Press Enter to close the browser...")
    driver.quit()