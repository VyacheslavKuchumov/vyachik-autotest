from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import time

import random

BASE_URL = "http://localhost:8080"



# Setup
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
# driver.maximize_window()  # Maximize window

def getClientElement():
    return EC.presence_of_element_located((By.ID, "ru.global-system.gl3.client"))

def getModalWindow():
    return EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'gwindow-modal')]"))

def generateObjectName():
    return f"TEST_OBJECT_{random.randint(0,100)}{random.randint(0,100)}{random.randint(0,100)}"

def generateReleaseName():
    return f"TEST_RELEASE_{random.randint(0,100)}{random.randint(0,100)}{random.randint(0,100)}"

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


class ToolBarBtn:
    EDIT_IN_LIST = "(//div[contains(@class, 'PToolButton')])[10]"
    INSERT = "(//div[contains(@class, 'PToolButton')])[7]"
    CREATE_RELEASE = "//div[contains(text(), 'Создать релиз')]"

def click(button):
    match button:
        case ToolBarBtn.EDIT_IN_LIST:
            btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, button))
            )
            btn.click()
        case ToolBarBtn.INSERT:
            btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, button))
            )
            btn.click()
        case ToolBarBtn.CREATE_RELEASE:
            btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, button))
            )
            btn.click()
            btn.click()
        case _ :
            pass

class HotKey:
    SAVE_FORM = Keys.LEFT_CONTROL + "s"
    INFO = Keys.LEFT_CONTROL + Keys.ALT + "i"
    EXIT = Keys.ESCAPE
    CHOOSE_MODAL = Keys.F2

def send_hot_key(key_combination):
    wait.until(getClientElement())
    body = wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, "body"))
    )
    body.click()
    body.send_keys(key_combination)

def enter_text(element: WebElement, text):
    wait.until(getClientElement())
    element.click()
    element.send_keys(text)
def clear_text(element: WebElement):
    wait.until(getClientElement())
    element.click()
    element.send_keys(Keys.LEFT_CONTROL+ "a" + Keys.BACKSPACE)
        

try:
    # Go to website
    driver.get(BASE_URL)

    login()
    
    goToPage("/PGDEV/Btk_ConfiguratorMainMenu/gtk-ru.bitec.app.btk.Btk_SettingGroup%23List/")

    click(ToolBarBtn.INSERT)

    system_name_field = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//input[@class='D56M6YB-t-c D56M6YB-t-h'])[3]"))
    )
    enter_text(system_name_field, generateObjectName())
    send_hot_key(HotKey.SAVE_FORM)

    wait.until(getModalWindow())

    click(ToolBarBtn.CREATE_RELEASE)

    release_name_field = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//input[contains(@value, 'Перенос конфигурации')])"))
    )

    clear_text(release_name_field)
    enter_text(release_name_field, generateReleaseName())
    send_hot_key(Keys.ENTER)

    send_hot_key(HotKey.CHOOSE_MODAL)
    send_hot_key(HotKey.CHOOSE_MODAL)

    time.sleep(2)
    
    send_hot_key(HotKey.CHOOSE_MODAL)
    time.sleep(5)
    send_hot_key(HotKey.SAVE_FORM)
    # goToPage("/PGDEV/Btk_ConfiguratorMainMenu/gtk-ru.bitec.app.btk.Btk_SettingGroup%23List/")
    
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Keep browser open for a while
    input("Press Enter to close the browser...")
    driver.quit()


