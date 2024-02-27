from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    purchaseButton = (By.CSS_SELECTOR, "input[type='submit']")
    success = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def get_purchase(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def confirm_success(self):
        # print("hello")
        return self.driver.find_element(*ConfirmPage.success)
