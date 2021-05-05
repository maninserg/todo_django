from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time


MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        """ open firefox """
        self.browser = webdriver.Firefox()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                # Check string in list table
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrive_it_later(self):

        # Test that 'ToDo' is in the title
        self.browser.get(self.live_server_url)
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
        inputbox.send_keys(Keys.ENTER)

        # Test that a table with tasks is on the home page and
        # there is task was typed before in the table
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # Test that a task can be typed
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Make mouschk by peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        # Test that a table with tasks is on the home page and
        # there is task was typed before in the table
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Make mouschk by peacock feathers')

    def test_multiple_users_can_starts_lists_at_different_urls(self):

        # User Alice go to our site and add task to her list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        alice_list_url = self.browser.current_url
        self.assertRegex(alice_list_url, '/lists/.+')

        # User Bob go to our site and add task to his list
        # And He can't see Alice's list of tasks

        self.browser.quit()
        self.browser = webdriver.Firefox()

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('Make mouschk by peacock feathers', page_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        bob_list_url = self.browser.current_url
        self.assertRegex(bob_list_url, '/lists/.+')
        self.assertNotEqual(alice_list_url, bob_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

    def test_lyout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024,768)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512, delta=10)

        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512, delta=10)


    def tearDown(self):
        """ close firefox """
        self.browser.quit()


if __name__ == "__main__":
    pass
