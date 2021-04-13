from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        """ open firefox """
        self.browser = webdriver.Firefox()

    def test_can_start_a_list_and_retrive_it_later(self):

        # Test that 'ToDo' is in the title
        self.browser.get('http:/localhost:8000')
        self.assertIn('ToDo', self.browser.title)

        # Test that 'ToDo' is in the heder in the home page
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('ToDo', header_text)

        # Test that an input box is on the home page
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')

        # Test that a task can be typed
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.Enter)

        # Time sleep for refreshing home page
        time.sleep(1)

        # Test that a table with tasks is on the home page and
        # there is task was typed before in the table
        table = self.browser.find_element_by_id('id_list_table')
        rows = self.browser.find_elements_by_tag_name('tr')
        self.assertTrue(any(row == '1: Buy peacock feathers' for row in rows))

    def tearDown(self):
        """ close firefox """
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
