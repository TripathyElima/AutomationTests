'''
Test case verifies that Keyword search from item page actually does ALL Category search instead of SUB Category search .
This test case fails in Amazon store currently 
Test Case runs fine and verified 
'''

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

PRODUCT_CODE = '6000086198866'
WALMART_URL = 'https://www.walmart.ca/en/ip'
HOME_PAGE_TITLE = 'Walmart'
ITEM_PAGE_TITLE = 'Teddy'
KEYWORD_FOR_SEARCH = 'pen'
SEARCH_ID = 'global-search'
TOTAL_PAGE_SEARCH_COUNT = './/span[@id = "shelf-sort-count"]/span'

class SearchPage(webdriver.Chrome):
	def __init__(self, url):
		super(SearchPage, self).__init__()
		self.implicitly_wait(10)
		self.get(url)

	def enter_keyword_for_search(self, keyword):
		global_search = browser.find_element_by_id(SEARCH_ID)
		global_search.send_keys(KEYWORD_FOR_SEARCH + Keys.RETURN)

	def match_search_result_count(self, total_records_homepage, total_records_item_page):
		if (total_records_homepage == total_records_item_page):
			return "Keyword search from item page is from all categories"
		else:
			return "Keyword search from item page is from sub categories"
					
if __name__ == "__main__":
	browser = SearchPage(WALMART_URL)
	assert HOME_PAGE_TITLE in browser.title
	browser.enter_keyword_for_search(KEYWORD_FOR_SEARCH)
	total_records_homepage = browser.find_elements_by_xpath(TOTAL_PAGE_SEARCH_COUNT)[2].text
	browser.get(WALMART_URL + "/" + PRODUCT_CODE)
	assert ITEM_PAGE_TITLE in browser.title
	browser.enter_keyword_for_search(KEYWORD_FOR_SEARCH)
	total_records_item_page = browser.find_elements_by_xpath(TOTAL_PAGE_SEARCH_COUNT)[2].text
	result = browser.match_search_result_count(total_records_homepage, total_records_item_page)
	assert not ('sub' in result)
	browser.quit()