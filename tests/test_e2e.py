from selenium.webdriver.common.by import By

from pageObjects.homePage import HomePage
from utilities.baseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        # creating HomePage object and calling the parameterized constructor
        homePage = HomePage(self.driver)

        # calling methods of HomePage class
        checkoutPage = homePage.shop_items()
        log.info("Shop items")

        # calling methods of CheckoutPage class
        cards = checkoutPage.get_card_titles()

        # items = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for card in cards:
            if checkoutPage.get_card_product(card).text == "Blackberry":
                checkoutPage.get_card_footer(card).click()
                break

        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        confirmPage = checkoutPage.get_final_checkout()

        self.driver.find_element(By.ID, 'country').send_keys("ind")

        self.verify_link_presence("India")

        countries = self.driver.find_elements(By.XPATH, "//div[@class='suggestions']/ul/li/a")

        for country in countries:
            if country.text == 'India':
                country.click()
                break

        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        # self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        confirmPage.get_purchase().click()

        self.verify_link_presence_success()
        assert "Thank you!" in confirmPage.confirm_success().text
