from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import random

BASE_URL = "http://localhost:8080"



# Setup
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
# driver.maximize_window()  # Maximize window

def getClientElement():
    return EC.presence_of_element_located((By.ID, "ru.global-system.gl3.client"))

def login():
    user_input = wait.until(
        EC.element_to_be_clickable((By.NAME, "j_username"))
    )
    user_input.send_keys(Keys.RETURN)
    wait.until(getClientElement())

def goToPage(url):
    driver.get(BASE_URL + url)
    wait.until(getClientElement())
    body = wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, "body"))
    )
    body.send_keys(Keys.RETURN)
    wait.until(getClientElement())

def generateObjectName():
    return f"TEST_OBJECT{random.randint(0,100)}{random.randint(0,100)}{random.randint(0,100)}"

class ToolBarBtn:
    EDIT_IN_LIST = "(//div[contains(@class, 'PToolButton')])[10]"
    INSERT = "(//div[contains(@class, 'PToolButton')])[7]"
    
class HotKey:
    SAVE_FORM = Keys.LEFT_CONTROL + "s"
    INFO = Keys.LEFT_CONTROL + Keys.ALT + "i"
    EXIT = Keys.ESCAPE

def click(button):
    match button:
        case ToolBarBtn.EDIT_IN_LIST:
            btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, ToolBarBtn.EDIT_IN_LIST))
            )
            btn.click()
        case ToolBarBtn.INSERT:
            btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, ToolBarBtn.INSERT))
            )
            btn.click()
        case _ :
            pass
def send_hot_key(key_combination):
    wait.until(getClientElement())
    body = wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, "body"))
    )
    body.send_keys(key_combination)

def enter_text(class_name, text):
    wait.until(getClientElement())
    text_field = wait.until(
        EC.element_to_be_clickable((By.XPATH, f"(//input[@class='{class_name}'])[3]"))
    )
    text_field.click()
    text_field.send_keys(text)
        

try:
    # Go to website
    driver.get(BASE_URL)

    login()
    
    goToPage("/PGDEV/Btk_ConfiguratorMainMenu/gtk-ru.bitec.app.btk.Btk_SettingGroup%23List/")

    click(ToolBarBtn.INSERT)


    enter_text("D56M6YB-t-c D56M6YB-t-h", generateObjectName())
    send_hot_key(HotKey.SAVE_FORM)
    
    send_hot_key(HotKey.INFO)
    # goToPage("/PGDEV/Btk_ConfiguratorMainMenu/gtk-ru.bitec.app.btk.Btk_SettingGroup%23List/")
    
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Keep browser open for a while
    input("Press Enter to close the browser...")
    driver.quit()


