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
    suburb_name = (By.XPATH, '//input[@placeholder="Suburb Name"]')
    service_area_tab = (By.XPATH, '//a[contains(text(), "Service Area")]')
    select_country = (By.XPATH, '//p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/p-dropdown[1]/div[1]/div[3]')
    search_country = (By.XPATH, "//input[@placeholder='Search Country']")
    country_list = (By.XPATH, '//div[@class="ui-dropdown-items-wrapper"]//ul//p-dropdownitem')
    element_list = (By.XPATH, '//li[@class="ui-dropdown-item ui-corner-all"]//span')
    select_state = (By.XPATH, '//p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/p-dropdown[1]/div[1]/div[3]')
    search_state = (By.XPATH, '//input[@placeholder="Search State"]')
    state_list = (By.XPATH, '//div[@class="ui-dropdown-items-wrapper"]//ul//p-dropdownitem')
    state_element_list = (By.XPATH, '//li[@class="ui-dropdown-item ui-corner-all"]//span')
    suburb_name1 = (By.XPATH, '//input[@placeholder="Enter Suburb"]')
    social_link_tab = (By.XPATH, '//a[contains(text(), "Social Link")]')
    select_social_media = (By.XPATH, '//p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/form[1]/div[1]/div[1]/div[1]/p-dropdown[1]/div[1]/div[3]')
    select_social_type = (By.XPATH, '//app-event-vendor-management[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/form[1]/div[1]/div[1]/div[1]/p-dropdown[1]/div[1]/div[4]/div[2]/ul[1]/p-dropdownitem[3]/li[1]')
    link_text_box = (By.ID, 'txtMediaType')
    add_link_button = (By.XPATH, '//a[@ptooltip="Add Link"]')
    bank_details_tab = (By.XPATH, '//a[contains(text(), "Bank Details")]')
    account_no = (By.ID, 'txtAccountNo')
    account_name = (By.ID, 'txtAccountName')
    account_type = (By.ID, 'txtAccType')
    bank_name = (By.ID, 'txtBankName')
    branch_name = (By.ID, 'txtBranchName')
    others_tab = (By.XPATH, '//a[contains(text(), "Other")]')
    alternate_mobile_no = (By.ID, 'txtAlternateMobileNo')
    alternate_mail_id = (By.ID, 'txtAlternateMailID')
    save_vendor_details = (By.XPATH, '//button[@data-tour="savevendorVMdetails"]')
    close_button = (By.XPATH, '//app-event-vendor-management[1]/app-addvendormodal[1]/div[2]/div[1]/div[1]/div[1]/div[1]')


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

    def Select_country(self):
        return self.driver.find_element(*Add_vendor.select_country)

    def Search_country(self):
        return self.driver.find_element(*Add_vendor.search_country)

    def Country_list(self):
        return self.driver.find_elements(*Add_vendor.country_list)

    def Element_list(self):
        return self.driver.find_elements(*Add_vendor.element_list)

    def Select_state(self):
        return self.driver.find_element(*Add_vendor.select_state)

    def Search_state(self):
        return self.driver.find_element(*Add_vendor.search_state)

    def State_list(self):
        return self.driver.find_elements(*Add_vendor.state_list)

    def State_element_list(self):
        return self.driver.find_elements(*Add_vendor.state_element_list)

    def Suburb_name1(self):
        return self.driver.find_element(*Add_vendor.suburb_name1)

    def Social_link_tab(self):
        return self.driver.find_element(*Add_vendor.social_link_tab)

    def Select_social_media(self):
        return self.driver.find_element(*Add_vendor.select_social_media)

    def Select_social_type(self):
        return self.driver.find_element(*Add_vendor.select_social_media)

    def Link_text_box(self):
        return self.driver.find_element(*Add_vendor.link_text_box)

    def Add_link_button(self):
        return self.driver.find_element(*Add_vendor.add_link_button)

    def Bank_details_tab(self):
        return self.driver.find_element(*Add_vendor.bank_details_tab)

    def Account_no(self):
        return self.driver.find_element(*Add_vendor.account_no)

    def Account_name(self):
        return self.driver.find_element(*Add_vendor.account_name)

    def Account_type(self):
        return self.driver.find_element(*Add_vendor.account_type)

    def Bank_name(self):
        return self.driver.find_element(*Add_vendor.bank_name)

    def Branch_name(self):
        return self.driver.find_element(*Add_vendor.branch_name)

    def Others_tab(self):
        return self.driver.find_element(*Add_vendor.others_tab)

    def Alternate_mobile_no(self):
        return self.driver.find_element(*Add_vendor.alternate_mobile_no)

    def Alternate_email_id(self):
        return self.driver.find_element(*Add_vendor.alternate_mail_id)

    def Save_detail_button(self):
        return self.driver.find_element(*Add_vendor.save_vendor_details)

    def Close_button(self):
        return self.driver.find_element(*Add_vendor.close_button)



