from selenium.webdriver.common.by import By

from pageObjects.confirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardProduct = (By.XPATH, "div/h4/a")
    cardFooter = (By.XPATH, "div[@class='card-footer']/button")
    checkoutButton = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    confirmCheckoutButton = (By.XPATH, "//button[@class='btn btn-success']")
    enterCountry  =(By.ID, 'country')
    countrySuggestion = (By.XPATH, "//div[@class='suggestions']")
    selectCountry = (By.XPATH, "//div[@class='suggestions']/ul/li/a")
    agreeTC = (By.XPATH, "//label[@for='checkbox2']")

    
    def get_card_titles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def get_card_product(self, item):
        return item.find_element(*CheckoutPage.cardProduct)

    def get_card_footer(self, item):
        return item.find_element(*CheckoutPage.cardFooter)

    def  get_final_checkout(self):
        self.driver.find_element(*CheckoutPage.confirmCheckoutButton).click()
        return ConfirmPage(self.driver)
