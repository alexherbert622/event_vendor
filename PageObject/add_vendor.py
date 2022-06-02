from selenium.webdriver.common.by import By


class Add_vendor:

    def __init__(self, driver):
        self.driver = driver

    add_button = (By.XPATH, '//a[@ptooltip="Add Vendor"]')
    title_click = (By.XPATH, '//p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/p-dropdown[1]/div[1]/div[3]')
    title_select = (By.XPATH, '//div[@class="ui-dropdown-items-wrapper"]//ul//p-dropdownitem[1]//li')
    firstname = (By.ID, 'txtFirstName')
    lastname = (By.ID, 'txtLastName')
    companyname = (By.ID, 'txtBusinessName')
    select_role_type = (By.XPATH, '//p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/p-dropdown[1]/div[1]/div[3]')
    type_click = (By.XPATH, '//div[@class="ui-dropdown-items-wrapper"]//ul//p-dropdownitem[2]//li')
    mailid = (By.ID, 'txtMailID')
    mobileno = (By.ID, 'txtMobileNo')
    website = (By.ID, 'txtWebsite')
    assign_item_click = (By.XPATH, '//angular2-multiselect[1]/div[1]/div[1]/div[1]')
    assign_item_select = (By.XPATH, '//angular2-multiselect[1]/div[1]/div[2]/div[3]/div[3]/ul[1]/span[2]/li[1]/label[1]')
    assign_tags = (By.XPATH, '//p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[12]/div[1]/mat-chip-list[1]/div[1]/input[1]')
    address_tab =(By.XPATH, '//a[contains(text(), "Address")]')
    search_address = (By.ID, 'txtAddress')
    country_name = (By.ID, 'txtCountry')
    state_name = (By.ID, 'txtState')
    suburb_name = (By.ID, 'txtSuburb')
    service_area_tab = (By.XPATH, '//a[contains(text(), "Service Area")]')

    def Add_button(self):
        return self.driver.find_element(*Add_vendor.add_button)

    def Title_click(self):
        return self.driver.find_element(*Add_vendor.title_click)

    def Title_select(self):
        return self.driver.find_element(*Add_vendor.title_select)

    def Firstname(self):
        return self.driver.find_element(*Add_vendor.firstname)

    def Lastname(self):
        return self.driver.find_element(*Add_vendor.lastname)

    def Companyname(self):
        return self.driver.find_element(*Add_vendor.companyname)

    def Select_role_type(self):
        return self.driver.find_element(*Add_vendor.select_role_type)

    def Type_click(self):
        return self.driver.find_element(*Add_vendor.type_click)

    def Mailid(self):
        return self.driver.find_element(*Add_vendor.mailid)

    def Mobileno(self):
        return self.driver.find_element(*Add_vendor.mobileno)

    def Website(self):
        return self.driver.find_element(*Add_vendor.website)

    def Assign_item_click(self):
        return self.driver.find_element(*Add_vendor.assign_item_click)

    def Assign_item_select(self):
        return self.driver.find_element(*Add_vendor.assign_item_select)

    def Assign_tags(self):
        return self.driver.find_element(*Add_vendor.assign_tags)

    def Address_tab(self):
        return self.driver.find_element(*Add_vendor.address_tab)

    def Search_address(self):
        return self.driver.find_element(*Add_vendor.search_address)

    def Country_name(self):
        return self.driver.find_element(*Add_vendor.country_name)

    def State_name(self):
        return self.driver.find_element(*Add_vendor.state_name)

    def Suburb_name(self):
        return self.driver.find_element(*Add_vendor.suburb_name)

    def Service_area_tab(self):
        return self.driver.find_element(*Add_vendor.service_area_tab)