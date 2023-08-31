from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePageLocators
from utils.CustomLogger import CustomLogger
logger = CustomLogger()


class GoogleSearchPageLocators(BasePageLocators):
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_RESULTS = (By.XPATH,"//div[@id='search']//div[@jscontroller and @jsaction and @style]")
    RESULT_TITLE = (By.CSS_SELECTOR,"h3")
    RESULT_URL = (By.CSS_SELECTOR,"a")
    RESULT_DESC = (By.CSS_SELECTOR,"div[style='-webkit-line-clamp:2']")


class GoogleSearchPage:
    def __init__(self, driver):
        self.driver = driver

    def search_for_keyword(self, keyword):
        self.driver.find_element(*GoogleSearchPageLocators.SEARCH_BOX).send_keys(keyword)
        logger.info("Arama Alanı Dolduruldu: ",keyword)
        self.driver.find_element(*GoogleSearchPageLocators.SEARCH_BOX).send_keys(Keys.RETURN)

    def get_search_results(self):
        search_results = self.driver.find_elements(*GoogleSearchPageLocators.SEARCH_RESULTS)
        logger.info('Arama Sonuçları Listelendi. Sonuç Sayısı: ', len(search_results))
        return search_results

    def parse_search_results(self, search_results):
        results = []
        for result in search_results:
            try:
                title = result.find_element(*GoogleSearchPageLocators.RESULT_TITLE).text
                url = result.find_element(*GoogleSearchPageLocators.RESULT_URL).get_attribute("href")
                description = result.find_element(*GoogleSearchPageLocators.RESULT_DESC).text
                logger.info("title: ",title)
                logger.info("url: ",url)
                logger.info("description: ",description)
                logger.info("------------------------")
                results.append({
                    "title": title,
                    "url": url,
                    "description": description
                })
            except:
                pass

        return results