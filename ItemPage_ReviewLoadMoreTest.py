'''
Test case verifies that with loading more review page rendering doesn't break
Test Case runs fine and verified
'''

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

PRODUCT_CODE = '6000195521502'
WALMART_URL = 'https://www.walmart.ca/en/ip'
REVIEW_BUTTON = './/button[@class = "review-link link-button"]'
LOAD_MORE_BUTTON = './/button[@class = "bv-content-btn bv-content-btn-pages bv-content-btn-pages-load-more bv-focusable"]'
FOOTER = 'global-footer'

class ImageSlider(webdriver.Chrome):
	def __init__(self, url):
		super(ImageSlider, self).__init__()
		self.implicitly_wait(10)
		self.get(url)
		
	def click_reviews_link(self):
		review_button = browser.find_element_by_xpath(REVIEW_BUTTON)
		review_button.click()
		
	def click_load_more_review(self):
		load_more = browser.find_element_by_xpath(LOAD_MORE_BUTTON)
		load_more.click()
		

if __name__ == "__main__":
	browser = ImageSlider(WALMART_URL + "/" + PRODUCT_CODE)
	browser.click_reviews_link()
	browser.click_load_more_review()
	# Verify that after load more, page footer exists
	if not (browser.find_element_by_id(FOOTER)):
		 raise AssertionError()
	browser.quit()