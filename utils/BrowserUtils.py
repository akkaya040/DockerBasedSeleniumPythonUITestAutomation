from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from utils.CustomLogger import CustomLogger
logger = CustomLogger()


class BrowserUtils(object):

    def __init__(self):
        self.driver = None

    def set_chrome_options(self) -> Options:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_prefs = {}
        chrome_options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        return chrome_options

    def set_firefox_options(self):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = True
        return firefox_options

    def get_browser(self, browsername):
        if browsername == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=self.set_firefox_options())
        elif browsername == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.set_chrome_options())
        else:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())

        logger.info("Selected Browser: ",browsername)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        return self.driver

