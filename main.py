from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import time
import random

from config import config

# Setup
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
# driver.maximize_window()  # Maximize window

def getMainFormElement():
    return EC.presence_of_element_located((By.ID, "ru.global-system.gl3.client"))

def getModalWindow():
    return EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'gwindow-modal')]"))

def generateCode():
    return f"{random.randint(100,999)}{random.randint(100,999)}{random.randint(100,999)}"

def login():
    driver.get(f"{config.BASE_URL}/{config.USERNAME}:{config.PASSWORD}@{config.DB}/{config.APP_NAME}/{config.START_FORM}")
    wait.until(getMainFormElement())

def goToPage(url):
    driver.get(config.BASE_URL + url)
    wait.until(getMainFormElement())
    body = wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, "body"))
    )
    body.send_keys(Keys.RETURN)
    wait.until(getMainFormElement())


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
    EDIT = Keys.F4

def send_hot_key(key_combination):
    wait.until(getMainFormElement())
    body = wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, "body"))
    )
    body.click()
    body.send_keys(key_combination)

def enter_text(element: WebElement, text):
    wait.until(getMainFormElement())
    element.click()
    element.send_keys(text)
def clear_text(element: WebElement):
    wait.until(getMainFormElement())
    element.click()
    element.send_keys(Keys.LEFT_CONTROL+ "a" + Keys.BACKSPACE)
        

try:

    login()
    

    click(ToolBarBtn.INSERT)

    system_name_field = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//input[@class='D56M6YB-t-c D56M6YB-t-h'])[3]"))
    )
    enter_text(system_name_field, "TEST_OBJECT_" + generateCode())
    send_hot_key(HotKey.SAVE_FORM)

    wait.until(getModalWindow())

    click(ToolBarBtn.CREATE_RELEASE)

    release_name_field = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//input[contains(@value, 'Перенос конфигурации')])"))
    )

    clear_text(release_name_field)
    enter_text(release_name_field, "TEST_RELEASE_" + generateCode())
    send_hot_key(Keys.ENTER)

    send_hot_key(HotKey.CHOOSE_MODAL)
    send_hot_key(HotKey.CHOOSE_MODAL)

    time.sleep(2)
    
    send_hot_key(HotKey.CHOOSE_MODAL)
    time.sleep(5)
    send_hot_key(HotKey.SAVE_FORM)
    
    
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Keep browser open for a while
    input("Press Enter to close the browser...")
    driver.quit()


