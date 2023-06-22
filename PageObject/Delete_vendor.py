from selenium.webdriver.common.by import By


class Delete_vendor:

    def __init__(self, driver):
        self.driver = driver

    vendor_name = (By.XPATH, '//div[3]//table[1]//tbody[1]//tr//td[2]')
    vendor_delete = (By.XPATH, '//td[@data-title="Action"]//div[1]//a[2]')
    confirm_delete = (By.XPATH, '//button[contains(text(), "Yes, Remove it!")]')
    vendor_name1 = (By.XPATH, '//app-event-vendor-management[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/table[1]/tbody[1]//tr//td[2]')
    vendor_delete1 = (By.XPATH, '//app-event-vendor-management[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/table[1]/tbody[1]//tr//td[8]//div//a[2]')
    vendor_delete4 = (By.XPATH, '//app-event-vendor-management[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[4]/td[8]/div[1]/a[2]/i[1]')

    def Vendor_name(self):
        return self.driver.find_elements(*Delete_vendor.vendor_name)

    def Vendor_delete(self):
        return self.driver.find_elements(*Delete_vendor.vendor_delete)

    def Confim_delete(self):
        return self.driver.find_element(*Delete_vendor.confirm_delete)

    def Vendor_name1(self):
        return self.driver.find_elements(*Delete_vendor.vendor_name1)

    def Vendor_delete1(self):
        return self.driver.find_elements(*Delete_vendor.vendor_delete1)

    def Vendor_delete4(self):
        return self.driver.find_element(*Delete_vendor.vendor_delete4)