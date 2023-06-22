from selenium.webdriver.common.by import By


class Clear_information:
    
    def __init__(self, driver):
        self.driver = driver

    details_button = (By.XPATH, '//div[3]//table[1]//tbody[1]//tr[1]//td[8]//div[1]//a[1]')
    edit_button = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/span[1]/a[1]')
    business_name = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/input[1]')
    mail_id = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/input[1]')
    mobile_no = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[7]/div[1]/input[1]')
    website = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[9]/div[1]/input[1]')
    assign_item = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[10]/div[1]/angular2-multiselect[1]/div[1]/div[1]/div[1]/span[1]/c-icon[1]')
    assign_item_checkbox_click = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[10]/div[1]/angular2-multiselect[1]/div[1]/div[2]/div[3]/div[3]/ul[1]/span[2]/li[1]/label[1]')
    assign_tags = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[12]/div[1]/mat-chip-list[1]/div[1]/input[1]')
    address_tab = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/nav[1]/div[1]/a[2]')
    search_address = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]')
    country_name = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/input[1]')
    state_name = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/input[1]')
    suburb_name = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/input[1]')
    service_area_tab = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/nav[1]/div[1]/a[3]')
    select_country = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/p-dropdown[1]/div[1]/div[3]')
    search_country = (By.XPATH, '//input[@placeholder="Search Country"]')
    country_list = (By.XPATH, '//div[@class="ui-dropdown-items-wrapper"]//ul//p-dropdownitem')
    country_select = (By.XPATH, '//li[@class="ui-dropdown-item ui-corner-all"]//span')
    select_state = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/p-dropdown[1]/div[1]/div[3]')
    search_state = (By.XPATH, '//input[@placeholder="Search State"]')
    state_list = (By.XPATH, '//div[@class="ui-dropdown-items-wrapper"]//ul//p-dropdownitem')
    state_select = (By.XPATH, '//li[@class="ui-dropdown-item ui-corner-all"]//span')
    enter_suburb = (By.XPATH, '//input[@placeholder="Enter Suburb"]')
    clear_suburb = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/p-chips[1]/div[1]/ul[1]/li[1]/span[1]')
    social_link_tab = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/nav[1]/div[1]/a[4]')
    select_social_media_type = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/form[1]/div[1]/div[1]/div[1]/p-dropdown[1]/div[1]/div[3]')
    select_social_type = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/form[1]/div[1]/div[1]/div[1]/p-dropdown[1]/div[1]/div[4]/div[2]/ul[1]/p-dropdownitem[3]/li[1]')
    enter_social_media = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]')
    add_social_media_button = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/form[1]/div[1]/div[3]/a[1]/i[1]')
    clear_social_link = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/form[1]/div[1]/div[4]/div[1]/span[1]/a[1]/i[1]')
    bank_details_tab = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/nav[1]/div[1]/a[5]')
    account_no = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/input[1]')
    account_name = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/input[1]')
    account_type = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[1]/input[1]')
    bank_name = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[4]/div[1]/input[1]')
    branch_name = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[5]/div[1]/input[1]')
    others_tab = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/nav[1]/div[1]/a[6]')
    alternate_mobile_no = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/input[1]')
    alternate_email_id = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form[1]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[2]/div[1]/input[1]')
    update_button = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-addvendormodal[1]/div[2]/div[1]/div[2]/div[3]/button[2]')
    vendor_profile_image = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/div[1]/div[1]/div[2]/div[1]/span[1]/i[1]')
    click_to_upload = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/div[3]/div[1]/div[2]/div[2]/dropzone[1]/div[1]/div[1]/div[1]')
    clear_profile_image = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/i[1]')
    message_tab = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/a[2]')
    send_message_button = (By.XPATH, '//button[contains(text(), "Send a Message")]')
    toclick = (By.XPATH, '//app-compose-mail[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/p-multiselect[1]/div[1]/div[3]')
    mailidselect = (By.XPATH, '//div[@class="ui-multiselect-items-wrapper"]//ul//p-multiselectitem[3]//li//div[1]//div[1]')
    toclose = (By.XPATH, '//a[@class="ui-multiselect-close ui-corner-all"]')
    subject = (By.XPATH, '//input[@data-tour="subjectMessagename"]')
    entityclick = (By.XPATH, '//app-compose-mail[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[5]/div[1]/p-dropdown[1]/div[1]/div[3]')
    entityselect = (By.XPATH, '//div[@class="ui-dropdown-items-wrapper"]//ul//p-dropdownitem[3]//li[1]')
    switch_to_frame = (By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]')
    body_text = (By.XPATH, '//body')
    send_key1 = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/app-compose-mail[1]/div[2]/div[1]/div[2]/div[3]/button[2]')
    files_tab = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/a[5]')
    attach_file_button = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/a[1]')
    attach_from_computer = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]')
    click_to_file_upload = (By.XPATH, '//div[contains(text(), "Click or drag file here to upload")]')
    file_delete = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/a[2]/i[1]')
    confirm_delete = (By.XPATH, '//button[contains(text(), "Yes, Delete it!")]')
    notes_tab = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/div[1]/div[2]/div[1]/nav[1]/div[1]/a[7]')
    add_notes = (By.XPATH, '//button[contains(text(), "Add Notes")]')
    add_notes_text_box = (By.XPATH, '//textarea[@data-tour="addnotesdecriptionVM"]')
    delete_note = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]/div[1]/div[2]/div[1]/div[1]/span[2]/span[2]/a[2]')
    back_button = (By.XPATH, '//app-event-vendor-management[1]/div[3]/app-vendorprofile[1]/section[1]/div[1]/div[1]/div[1]/div[1]/button[1]')

    def Detail_button(self):
        return self.driver.find_element(*Clear_information.details_button)

    def Edit_button(self):
        return self.driver.find_element(*Clear_information.edit_button)

    def Business_name(self):
        return self.driver.find_element(*Clear_information.business_name)

    def Mail_id(self):
        return self.driver.find_element(*Clear_information.mail_id)

    def Mobile_no(self):
        return self.driver.find_element(*Clear_information.mobile_no)

    def Website(self):
        return self.driver.find_element(*Clear_information.website)

    def Assign_item(self):
        return self.driver.find_element(*Clear_information.assign_item)

    def Assign_item_checkbox_click(self):
        return self.driver.find_element(*Clear_information.assign_item_checkbox_click)

    def Assign_tags(self):
        return self.driver.find_element(*Clear_information.assign_tags)

    def Address_tab(self):
        return self.driver.find_element(*Clear_information.address_tab)

    def Search_address(self):
        return self.driver.find_element(*Clear_information.search_address)

    def Country_name(self):
        return self.driver.find_element(*Clear_information.country_name)

    def State_name(self):
        return self.driver.find_element(*Clear_information.state_name)

    def Suburb_name(self):
        return self.driver.find_element(*Clear_information.suburb_name)

    def Service_area_tab(self):
        return self.driver.find_element(*Clear_information.service_area_tab)

    def Select_country(self):
        return self.driver.find_element(*Clear_information.select_country)

    def Search_country(self):
        return self.driver.find_element(*Clear_information.search_country)

    def Country_list(self):
        return self.driver.find_elements(*Clear_information.country_list)

    def Country_select(self):
        return self.driver.find_elements(*Clear_information.country_select)

    def Select_state(self):
        return self.driver.find_element(*Clear_information.select_state)

    def Search_state(self):
        return self.driver.find_element(*Clear_information.search_state)

    def State_list(self):
        return self.driver.find_elements(*Clear_information.state_list)

    def State_select(self):
        return self.driver.find_elements(*Clear_information.state_select)

    def Enter_suburb(self):
        return self.driver.find_element(*Clear_information.enter_suburb)

    def Clear_suburb(self):
        return self.driver.find_element(*Clear_information.clear_suburb)

    def Social_link_tab(self):
        return self.driver.find_element(*Clear_information.social_link_tab)

    def Select_social_media_type(self):
        return self.driver.find_element(*Clear_information.select_social_media_type)

    def Select_social_type(self):
        return self.driver.find_element(*Clear_information.select_social_type)

    def Enter_social_media(self):
        return self.driver.find_element(*Clear_information.enter_social_media)

    def Add_social_media_button(self):
        return self.driver.find_element(*Clear_information.add_social_media_button)

    def Clear_social_link(self):
        return self.driver.find_element(*Clear_information.clear_social_link)

    def Bank_details_tab(self):
        return self.driver.find_element(*Clear_information.bank_details_tab)

    def Account_no(self):
        return self.driver.find_element(*Clear_information.account_no)

    def Account_name(self):
        return self.driver.find_element(*Clear_information.account_name)

    def Account_type(self):
        return self.driver.find_element(*Clear_information.account_type)

    def Bank_name(self):
        return self.driver.find_element(*Clear_information.bank_name)

    def Branch_name(self):
        return self.driver.find_element(*Clear_information.branch_name)

    def Other_tab(self):
        return self.driver.find_element(*Clear_information.others_tab)

    def Alternate_mobile_no(self):
        return self.driver.find_element(*Clear_information.alternate_mobile_no)

    def Alternate_email_id(self):
        return self.driver.find_element(*Clear_information.alternate_email_id)

    def Update_button(self):
        return self.driver.find_element(*Clear_information.update_button)

    def Vendor_profile_image(self):
        return self.driver.find_element(*Clear_information.vendor_profile_image)

    def Click_to_upload(self):
        return self.driver.find_element(*Clear_information.click_to_upload)

    def Clear_profile_image(self):
        return self.driver.find_element(*Clear_information.clear_profile_image)

    def Message_tab(self):
        return self.driver.find_element(*Clear_information.message_tab)

    def Send_message_button(self):
        return self.driver.find_element(*Clear_information.send_message_button)

    def Toclick(self):
        return self.driver.find_element(*Clear_information.toclick)

    def Mailidselect(self):
        return self.driver.find_element(*Clear_information.mailidselect)

    def Toclose(self):
        return self.driver.find_element(*Clear_information.toclose)

    def Subject(self):
        return self.driver.find_element(*Clear_information.subject)

    def Entityclick(self):
        return self.driver.find_element(*Clear_information.entityclick)

    def Entityselect(self):
        return self.driver.find_element(*Clear_information.entityselect)

    def Switch_to_frame(self):
        return self.driver.find_element(*Clear_information.switch_to_frame)

    def Body_text(self):
        return self.driver.find_element(*Clear_information.body_text)

    def Send_key1(self):
        return self.driver.find_element(*Clear_information.send_key1)

    def Files_tab(self):
        return self.driver.find_element(*Clear_information.files_tab)

    def Attach_file_button(self):
        return self.driver.find_element(*Clear_information.attach_file_button)

    def Attach_from_computer(self):
        return self.driver.find_element(*Clear_information.attach_from_computer)

    def Click_to_file_upload(self):
        return self.driver.find_element(*Clear_information.click_to_file_upload)

    def File_delete(self):
        return self.driver.find_element(*Clear_information.file_delete)

    def Confirm_delete(self):
        return self.driver.find_element(*Clear_information.confirm_delete)

    def Notes_tab(self):
        return self.driver.find_element(*Clear_information.notes_tab)

    def Add_notes(self):
        return self.driver.find_element(*Clear_information.add_notes)

    def Add_notes_text_box(self):
        return self.driver.find_element(*Clear_information.add_notes_text_box)

    def Delete_note(self):
        return self.driver.find_element(*Clear_information.delete_note)

    def Back_button(self):
        return self.driver.find_element(*Clear_information.back_button)
