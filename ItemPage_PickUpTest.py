'''
Test case verifies that with updating pick up zipcode location also updates
Test Case needs to investigated and it fails with element not visible error
'''

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

PRODUCT_CODE = '6000086198866'
WALMART_URL = 'https://www.walmart.ca/en/ip'
PICKUP_BUTTON = 'pf-tab-pickup'
PICKUP_LINK = 'reverse-anchor'
ZIPCODE_INPUT = 'postal-code-input'
POSTAL_CODE = 'L5N8N1'
PICK_UP_ADDRESS = './/table[@id = "tab-fulfillment-pickup"]/tbody/tr/td/p'
PICK_UP_LOCATION = '3155 Argentia Road'


class PickUpLocation(webdriver.Chrome):
	def __init__(self, url):
		super(PickUpLocation, self).__init__()
		self.implicitly_wait(10)
		self.get(url)
		
	def click_pick_up_link(self):
		pickUp_button = browser.find_element_by_id(PICKUP_BUTTON)
		pickUp_button.click()
		
	def update_pick_up_zip_code(self):
		zipCode_button = browser.find_element_by_class_name(PICKUP_LINK)
		zipCode_button.click()
		global_search = browser.find_element_by_id(ZIPCODE_INPUT)
		global_search.send_keys(POSTAL_CODE + Keys.RETURN)

		
if __name__ == "__main__":
	browser = PickUpLocation(WALMART_URL + "/" + PRODUCT_CODE)
	browser.click_pick_up_link()
	browser.update_pick_up_zip_code()
	#Verify that with ZIP update pick location also changes 
	if (browser.find_element_by_css_selector(PICK_UP_ADDRESS) != PICK_UP_LOCATION):
		raise AssertionError()
	browser.quit()