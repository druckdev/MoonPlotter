import time
from get_gecko_driver import GetGeckoDriver
from selenium import webdriver

MB_URL = "https://www.moonboard.com"

# try installing GeckoDriver if installed with pip
try:
    get_driver = GetGeckoDriver()
    get_driver.install()
except:
    pass

# Use the installed GeckoDriver with Selenium
driver = webdriver.Firefox()
driver.get(MB_URL)
time.sleep(3)
driver.quit()