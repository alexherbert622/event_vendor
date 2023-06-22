from selenium.webdriver.common.by import By


class Search_vendor:

    def __init__(self, driver):
        self.driver = driver

    search_vendor_textbox = (By.XPATH, '//app-event-vendor-management[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]')
    search_vendor_tab = (By.XPATH, '//a[@data-tour="searchvendoractionVM"]')
    vendor_name_list = (By.XPATH, '//div[@class="tab-pane fade show active"]//div[1]//div[1]//div[3]//table[1]//tbody[1]//tr//td[2]')
    vendor_name = (By.XPATH, '//td[@data-title="Action"]//div[1]//button')
    event_vendor_tab = (By.XPATH, '//a[contains(text(), "Event Vendor")]')

    def Search_vendor_textbox(self):
        return self.driver.find_element(*Search_vendor.search_vendor_textbox)

    def Search_vendor_tab(self):
        return self.driver.find_element(*Search_vendor.search_vendor_tab)

    def Vendor_name_list(self):
        return self.driver.find_elements(*Search_vendor.vendor_name_list)

    def Vendor_name(self):
        return self.driver.find_elements(*Search_vendor.vendor_name)

    def Event_vendor_tab(self):
        return self.driver.find_element(*Search_vendor.event_vendor_tab)