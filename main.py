from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BASE_URL = "http://localhost:8080"

class ToolBarBtn:
    EDIT_IN_LIST = "(//div[contains(@class, 'PToolButton')])[10]"
    INSERT = "(//div[contains(@class, 'PToolButton')])[7]"

# Setup
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
# driver.maximize_window()  # Maximize window

def get_client_element():
    return EC.presence_of_element_located((By.ID, "ru.global-system.gl3.client"))
    

def login():
    user_input = wait.until(
        EC.element_to_be_clickable((By.NAME, "j_username"))
    )
    user_input.send_keys(Keys.RETURN)
    wait.until(get_client_element())

def goToPage(url):
    driver.get(BASE_URL + url)
    wait.until(get_client_element())
    body = wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, "body"))
    )
    body.send_keys(Keys.RETURN)
    wait.until(get_client_element())

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
        

try:
    # Go to website
    driver.get(BASE_URL)

    login()
    
    goToPage("/PGDEV/Btk_ConfiguratorMainMenu/gtk-ru.bitec.app.btk.Btk_SettingGroup%23List/")

    click(ToolBarBtn.EDIT_IN_LIST)
    click(ToolBarBtn.INSERT)

    
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Keep browser open for a while
    input("Press Enter to close the browser...")
    driver.quit()


