import time


from base.PageFactory import PageFactory
from selenium.webdriver.common.keys import Keys


class CluePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.driver = driver
        self.timeout = 15
        self.highlight = True
        self.mobile_test = False

    locators = {
        "allTopic": ('XPATH', '//a[normalize-space()="All Topics"]'),
        "sortOption": ('XPATH', '//select[@aria-labelledby="sort-by"]'),
        "doneBtn": ('XPATH', '//button[normalize-space()="Done"]'),
        "searchField": ('XPATH', '//input[@aria-label="filter"]'),
        "subTopicNames": ('XPATH', '//div[@class="css-1k5s00q"]//div/child::p[1]')
    }

    def clueSearch(self, topic):
        # set_text(), click_button() methods are extended methods in PageFactory
        self.allTopic.click_button()
        self.searchField.set_text(topic)
        time.sleep(2.4)
        self.searchField.set_text(Keys.RETURN)
        time.sleep(2.4)
        time.sleep(2.4)

        textbox_username_id = "//a[normalize-space()='" + topic + "']"

        element_field = self.driver.find_element("xpath", textbox_username_id)

        element_field.visibility_of_element_located()

        element_field.click()
        time.sleep(2.4)
        subTopicSize = 0

        for element in self.subTopicNames:
            print(element)



