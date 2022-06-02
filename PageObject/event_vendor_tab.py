from selenium.webdriver.common.by import By


class Event_vendor_tab:

    def __init__(self, driver):
        self.driver = driver

    event_vendor_tab = (By.XPATH, '//div[@class="event-menu-nw"]//span[1]//ul//li[11]//a')

    def Event_vendor_tab(self):
        return self.driver.find_element(*Event_vendor_tab.event_vendor_tab)