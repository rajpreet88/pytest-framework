import time

import pytest

from pageObjects.homePage import HomePage
from testData.homePageTestData import HomePageTestData
from utilities.baseClass import BaseClass


class TestHomePage(BaseClass):

    def test_sign_in(self, get_data):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.get_name().send_keys(get_data["fname"])
        homePage.get_email().send_keys(get_data["email"])
        log.info("Getting the" + get_data["email"])
        homePage.get_example_check().click()
        self.select_options(homePage.get_gender(), get_data["gender"])
        homePage.get_submit().click()

        alertText = homePage.get_alert().text

        assert ("Success" in alertText)
        time.sleep(3)
        self.driver.refresh()

    @pytest.fixture(params=HomePageTestData.get_excel_data())
    def get_data(self, request):
        return request.param
