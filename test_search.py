import sys
import unittest

from utils.BrowserUtils import BrowserUtils
from pages.google_search_page import GoogleSearchPage
from pages.yahoo_search_page import YahooSearchPage
from utils.CustomLogger import CustomLogger
logger = CustomLogger()

class TestSearch(unittest.TestCase):
    def setUp(self):
        logger.info('setUp()')
        logger.info('Tests have been started...')
        self.driver =  BrowserUtils().get_browser(sys.argv[1])
        self.keyword = sys.argv[2]
        self.browser = sys.argv[1]

    def test_search_comparison(self):
        logger.info('test_search_comparison()')
        google_page = GoogleSearchPage(self.driver)
        yahoo_page = YahooSearchPage(self.driver)

        logger.info("Google Arama İşlemleri...")
        google_page.driver.get("https://www.google.com.tr")
        google_page.search_for_keyword(self.keyword)
        google_results = google_page.get_search_results()
        parsed_google_results = google_page.parse_search_results(google_results)
        logger.info("Google Arama İşlemleri tamamlandı.")

        logger.info("Yahoo Arama İşlemleri...")
        yahoo_page.driver.get("https://tr.search.yahoo.com/")  # Yahoo'nun URL'sini kullanın
        yahoo_page.search_for_keyword(self.keyword)
        yahoo_results = yahoo_page.get_search_results()
        parsed_yahoo_results = yahoo_page.parse_search_results(yahoo_results)
        logger.info("Yahoo Arama İşlemleri tamamlandı.")

        # Compare results
        logger.info("Sonuçlar Karşılaştırılıyor.")

        # Verileri karşılaştırmak için geçici bir set
        url_set = set()

        # Aynı URL'ye sahip sonuçları tutmak için bir liste
        same_url_results = []

        # parsed_google_results içindeki sonuçları dolaşır ve set'e ekleriz
        for item in parsed_google_results:
            if item is None:  # Eğer item None ise, bu öğeyi atlayarak bir sonraki öğeye geç
                continue
            url_set.add(item["url"])

        # parsed_yahoo_results içindeki sonuçlar
        for item in parsed_yahoo_results:
            if item is None:  # Eğer item None ise, bu öğeyi atlayarak bir sonraki öğeye geç
                continue
            if item["url"] in url_set:
                same_url_results.append(item)

        logger.info("Results with the same URL:")
        for result in same_url_results:
            logger.info("--------------------")
            logger.info("Title:", result["title"])
            logger.info("URL:", result["url"])
            logger.info("Description:", result["description"])
            logger.info("--------------------")

    def tearDown(self):
        logger.info('tearDown()')
        self.driver.quit()





if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
