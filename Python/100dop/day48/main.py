from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SeleniumBasics:

    PYTHON_WEB_PAGE = "https://www.python.org/"
    GOOGLE_WEB_PAGE = "https://www.google.com/"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def __del__(self):
        if self.driver:
            self.driver.quit()

    def find_python_events_directly(self):
        """Find elements on web page directly"""

        events_xpath = '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li'
        events = {}

        self.driver.get(self.PYTHON_WEB_PAGE)
        event_elements = self.driver.find_elements(By.XPATH, events_xpath)

        for element in event_elements:
            event_date = element.find_element(By.CSS_SELECTOR, 'time').get_attribute("datetime").split("T")[0]
            event_name = element.find_element(By.CSS_SELECTOR, 'a').text
            events[event_name] = event_date

        return events

    def filling_clicking(self):
        """Find and go to python.org using google"""
        self.driver.get(self.GOOGLE_WEB_PAGE)

        agreement_button_xpath = '//*[@id="L2AGLb"]'
        agreement_button = self.driver.find_element(By.XPATH, agreement_button_xpath)
        agreement_button.click()

        input_element_xpath = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
        input_element = self.driver.find_element(By.XPATH, input_element_xpath)
        input_element.send_keys("python")
        input_element.send_keys(Keys.ENTER)

        link_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Python.org")
        link_element.click()


if __name__ == '__main__':
    sel = SeleniumBasics()
    sel.filling_clicking()
    print(sel.find_python_events_directly())
    del sel
