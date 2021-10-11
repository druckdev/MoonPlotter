from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from os.path import isdir

getGecko_installed = True
try:
    from get_gecko_driver import GetGeckoDriver
except BaseException:
    getGecko_installed = False


class Scraper:

    def __init__(self, DEBUG: bool):
        self.MB_URL = "https://www.moonboard.com"
        self.DEBUG = DEBUG

        # use getGecko to get the driver
        if getGecko_installed:
            print("Getting GeckoDriver")
            get_driver = GetGeckoDriver()
            get_driver.install()

    def fetch_data(self, USERNAME: str, PASSWORD: str) -> dict:

        # use the installed GeckoDriver with Selenium
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless = not self.DEBUG
        driver = webdriver.Firefox(options=fireFoxOptions)

        driver.get(self.MB_URL)

        # login
        driver.find_element_by_id("loginDropdown").click()
        driver.find_element_by_id("Login_Username").send_keys(USERNAME)
        driver.find_element_by_id("Login_Password").send_keys(PASSWORD)
        driver.find_element_by_id("navlogin").click()

        time.sleep(10)  # TODO: await properly

        # navigate to logbook
        driver.find_element_by_id("llogbook").click()
        driver.find_element_by_link_text("VIEW").click()

        time.sleep(10)  # TODO: await properly

        # select version
        select = Select(driver.find_element_by_id("Holdsetup"))
        select.select_by_index(1)  # 2019 version TODO : more stable

        time.sleep(1)  # TODO: await properly

        main_section = driver.find_element_by_id("main-section")

        # get a tag expanders for the various days
        expanders = driver.find_elements_by_xpath(
            "//a[@class='k-icon k-i-expand']")
        res = []
        for a_tag in expanders:
            a_tag.click()  # expand information

            # get all entries for that day
            entries = main_section.find_elements_by_class_name("entry")

            for entry in entries:
                # get data
                if not entry.text in res:
                    res.append(entry.text)

        # process data
        formatted_data = []

        for data in res:
            data_arr = data.split('\n')
            formatted = {
                'Name': data_arr[0],
                'Setter': data_arr[1],
                'Grade': data_arr[2].split('.')[0]
            }
            formatted_data.append(formatted)

        # cleanup
        driver.quit()

        return formatted_data
