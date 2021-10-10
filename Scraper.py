from selenium import webdriver
import time
from os.path import isdir
import sys
import getopt

getGecko_installed = True
try:
    from get_gecko_driver import GetGeckoDriver
except BaseException:
    getGecko_installed = False


MB_URL = "https://www.moonboard.com"

# process arguments
(OPT, _) = getopt.getopt(sys.argv[1:], "d", "debug")

def find_key(arr, elem): return any(elem in sub for sub in arr)

DEBUG = find_key(OPT, '-d')

# use getGecko to get the driver
if getGecko_installed:
    print("Getting GeckDriver")
    get_driver = GetGeckoDriver()
    get_driver.install()

# use the installed GeckoDriver with Selenium
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.headless = not DEBUG
driver = webdriver.Firefox(options=fireFoxOptions)

driver.get(MB_URL)
time.sleep(3)
driver.quit()

# login
# form id : logindropdown
