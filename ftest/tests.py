from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase 

class PageTest(LiveServerTestCase):

	
	def setUp(self):
		self.browser = webdriver.Firefox()
		

	def test_browser_title(self):
		self.browser.get(self.live_server_url)
		self.assertIn('ATTENDANCE NATIN TO!', self.browser.title)

		tText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('WELCOME TO ATTENDANCE FORM', tText) 
		
		ptext = self.browser.find_element_by_tag_name('p').text
		self.assertIn('"Attend Today, Achive Tomorrow"', ptext)
		
		form = self.browser.find_element_by_tag_name('form') 

		l1 = self.browser.find_element_by_id('names').text
		self.assertIn('Name:', l1)

		l2 = self.browser.find_element_by_id('subjects').text
		self.assertIn('Subject:', l2)

		l3 = self.browser.find_element_by_id('bodies').text
		self.assertIn('Section:', l3)

		l4 = self.browser.find_element_by_id('dates').text
		self.assertIn('Date', l4) 

		Essential = self.browser.find_element_by_id('male').click()
		time.sleep(1)
		Essential = self.browser.find_element_by_id('female').click()
		time.sleep(1) 

		input1 = self.browser.find_element_by_id('name')
		self.assertEqual(input1.get_attribute('placeholder'),'Enter Name')
		input1 = self.browser.find_element_by_id('name').send_keys("Russel")
		time.sleep(1)
		input2 = self.browser.find_element_by_id('subject')
		self.assertEqual(input2.get_attribute('placeholder'),'Enter Subject')
		input2 = self.browser.find_element_by_id('subject').send_keys("Math") 
		time.sleep(1)    
		input3 = self.browser.find_element_by_id('body') 
		self.assertEqual(input3.get_attribute('placeholder'),'Enter body text')
		input3 = self.browser.find_element_by_id('body').send_keys("BSIE-ICT-3A") 
		time.sleep(1)

		date = self.browser.find_element_by_id('date').click()
		time.sleep(1)
		date = self.browser.find_element_by_id('date').send_keys("2012-11-02")
		time.sleep(1)

		submit = self.browser.find_element_by_id('ggg').click()
		time.sleep(1)

		nextpage = self.browser.current_url
		self.assertRegex(nextpage, '/goods/')
		

		self.browser.quit()	
		
		self.browser = webdriver.Firefox()
		self.browser.get(self.live_server_url)

		Essential = self.browser.find_element_by_id('male').click()
		time.sleep(1)
		Essential = self.browser.find_element_by_id('female').click()
		time.sleep(1) 

		input1 = self.browser.find_element_by_id('name')
		self.assertEqual(input1.get_attribute('placeholder'),'Enter Name')
		input1 = self.browser.find_element_by_id('name').send_keys("Adrianne")
		time.sleep(1)
		input2 = self.browser.find_element_by_id('subject')
		self.assertEqual(input2.get_attribute('placeholder'),'Enter Subject')
		input2 = self.browser.find_element_by_id('subject').send_keys("English") 
		time.sleep(1)    
		input3 = self.browser.find_element_by_id('body') 
		self.assertEqual(input3.get_attribute('placeholder'),'Enter body text')
		input3 = self.browser.find_element_by_id('body').send_keys("BSIE-ICT-3B") 
		time.sleep(1)

		date = self.browser.find_element_by_id('date').click()
		time.sleep(1)
		date = self.browser.find_element_by_id('date').send_keys("2001-12-15")
		time.sleep(1)

		submit = self.browser.find_element_by_id('ggg').click()
		time.sleep(1)  
		
		nextpage = self.browser.current_url
		self.assertRegex(nextpage, '/goods/')
		
		self.browser.quit()	


# if __name__ == '__main__':
# 	unittest.main()