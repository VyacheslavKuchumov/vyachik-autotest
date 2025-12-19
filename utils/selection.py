from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import JavascriptException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
import time

class Selection:
    def __init__(self, driver: WebDriver, main_form: WebElement, selection: WebElement):
        self.driver = driver
        self.main_form = main_form
        self.selection = selection
        
        
    def execute_jexl(self, jexl_script, timeout=30, dom_stability_delay=2):
        """
        Execute JEXL script on a web element and wait for conditions
        
        Args:
            jexl_script: The JEXL script to execute
            timeout: Maximum time to wait for conditions
            dom_stability_delay: Time to wait for DOM stability after execution
        """
        try:
            # Execute the async JavaScript
            async_script = """
            var callback = arguments[arguments.length - 1];
            callback(arguments[0].executeJexl(arguments[1]));
            """
            
            # Execute the async script
            result = self.driver.execute_async_script(
                async_script, 
                self.selection, 
                jexl_script
            )
            
            # Wait for JEXL execution to complete
            if self.main_form:
                # Wait for the data-selection-jexl-inprogress attribute to be false
                self._wait_for_jexl_completion(timeout)
            
            # Wait for DOM stability (simplified - you might need more sophisticated approach)
            time.sleep(dom_stability_delay)
            
            return result
            
        except JavascriptException as ex:
            # Handle JavaScript exceptions
            # You might want to check server settings here if available
            print(f"Javascript exception: {ex}")
            raise
    
    def _wait_for_jexl_completion(self, timeout):
        """Wait for JEXL execution to complete by checking attribute"""
        wait = WebDriverWait(self.driver, timeout)
        
        # Wait until the attribute is set to false or not present
        try:
            wait.until(
                lambda driver: self.main_form.get_attribute("data-selection-jexl-inprogress") == "false" 
                or not self.main_form.get_attribute("data-selection-jexl-inprogress")
            )
        except TimeoutException:
            print("Timeout waiting for JEXL completion")
            raise
    



