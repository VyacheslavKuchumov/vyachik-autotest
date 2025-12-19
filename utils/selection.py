from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import JavascriptException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
import time

class Selection:
    def __init__(self, driver: WebDriver, main_form_element: WebElement, selection_element: WebElement):
        self.driver = driver
        self.main_form_element = main_form_element
        self.selection = selection_element
        
        
    def execute_jexl(self, jexl_script: str, timeout=30, dom_stability_delay=2):
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
            if self.main_form_element:
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
                lambda driver: self.main_form_element.get_attribute("data-selection-jexl-inprogress") == "false" 
                or not self.main_form_element.get_attribute("data-selection-jexl-inprogress")
            )
        except TimeoutException:
            print("Timeout waiting for JEXL completion")
            raise

    def execute_operation(self, operation_name: str):
        """
        Execute an operation on a web element
        
        Args:
            operation_name: The name of the operation to execute
        """
        try:
            # Execute the async JavaScript
            async_script = """
            var callback = arguments[arguments.length - 1];
            callback(arguments[0].executeOperation(arguments[1]));
            """
            
            # Execute the async script
            result = self.driver.execute_async_script(
                async_script, 
                self.selection, 
                operation_name
            )
            
            return result
            
        except JavascriptException as ex:
            # Handle JavaScript exceptions
            # In Java, this checks server settings, but in Python we'll just raise an exception
            # You might want to add your own logic here based on your application's settings
            print(f"Javascript exception during operation execution: {ex}")
            # You could add logic here to check if operation execution is enabled
            # For now, we'll just re-raise the exception
            raise
    



