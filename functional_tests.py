from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        """ open firefox """
        self.browser = webdriver.Firefox()

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get("http:/localhost:8000")
        self.assertIn("ToDo", self.browser.title)

    def tearDown(self):
        """ close firefox """
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()
