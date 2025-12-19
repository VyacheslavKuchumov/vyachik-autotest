from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from utils.selection import Selection
from utils.element_finder import ElementFinder

from utils.config import config

class ActionManager:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.elementFinder = ElementFinder(self.driver)

    def login(self):
        self.driver.get(f"{config.BASE_URL}/{config.USER}:{config.PASSWORD}@{config.DB}/{config.APP_NAME}/{config.START_FORM}")
    
    def logout(self):
        mainForm = self.elementFinder.getMainFormElement()
        mainSelection = self.elementFinder.getSelectionElement(mainForm)
        selection = Selection(self.driver, mainForm, mainSelection)
        selection.execute_operation("MM_FILE_EXIT")
        