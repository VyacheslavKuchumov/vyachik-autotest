from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class ElementFinder:
    APPLICATION = "//div[@data-node.class='PApplication']"
    MAIN_FORM = "//div[@data-form.opentype='MAIN_FORM']"
    MAIN_SELECTION = "//div[@data-node.class='PSelection']"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def waitForApplicationPresence(self):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.APPLICATION))
        )
    
    def getMainFormElement(self) -> WebElement:
        self.waitForApplicationPresence()
        return self.driver.find_element(By.XPATH, self.MAIN_FORM)
    
    def getMainSelectionElement(self, main_form: WebElement) -> WebElement:
        self.waitForApplicationPresence()
        return main_form.find_element(By.XPATH, self.MAIN_SELECTION)