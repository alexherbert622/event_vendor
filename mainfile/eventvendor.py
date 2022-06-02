####################
# Name:event vendor module
# Description: To do some operation
# Author: Alex herbert
# Date: 23-05-2022
####################
# Library use #
import time
import os
import sys
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.Popupwindow import Popupwindow
from PageObject.add_vendor import Add_vendor
from PageObject.event_vendor_tab import Event_vendor_tab
from PageObject.eventdiarypage import eventdiarypage
from PageObject.login_page import Loginpage
from Testdata.datareadwritefile import Datareadfile, usernamepass, passwordpass, datawritefail, loggedinpass
from Utilities.BaseClass import Baseclass


@allure.severity(allure.severity_level.NORMAL)
class TestEpo(Baseclass):
    @allure.description('To enter the valid username')
    def test_TC_02_username(self):
        log = self.loggerdemo()
        datareadusername = Datareadfile.username
        loginpage = Loginpage(self.driver)
        wait = WebDriverWait(self.driver, 6)
        wait.until(EC.presence_of_element_located((By.NAME, "userNameOrEmail")))
        loginpage.usernameoremail().send_keys(datareadusername)
        usernamepass()

    @allure.description('To enter the valid password')
    def test_Test_03_password(self):
        loginpage = Loginpage(self.driver)
        datareadpwd = Datareadfile.password
        loginpage.password().send_keys(datareadpwd)
        passwordpass()


    try:
        @allure.description('only login when entered a valid password')
        def test_TC_04_login_button(self):
            loginpage = Loginpage(self.driver)
            loginpage.loginbutton().click()
            time.sleep(5)
    except Exception as e:
        def test_failedcase(self):
            allure.attach(self.driver.get_screenshot_as_png(), name="testfailedscreen",
                        attachment_type=AttachmentType.PNG)
            msg2 = datawritefail()
            self.driver.close()
    finally:
        @allure.description('Once logged in successfully to take a screenshot')
        def test_TC_05_screen_shot(self):
            allure.attach(self.driver.get_screenshot_as_png(), name="testscreenshot",
                      attachment_type=AttachmentType.PNG)

    @allure.description('To close the popup window')
    def test_TC_06_popup_window(self):
        popupwindow = Popupwindow(self.driver)
        popupwindow.popup().click()

    @allure.description('when successfully logged in to check the title for confirmation')
    def test_TC_07_logged_conformation(self):
        title1 = self.driver.title
        if title1 == "Event Plan On":
            print("logged in successfully")
            msg1 = loggedinpass()
        else:
            msg2 = datawritefail()

    @allure.description('To click the desired event')
    def test_TC_08_event_diary(self):
        eventdiary = eventdiarypage(self.driver)
        time.sleep(3)
        eventdiary.eventdiarytask().click()

    @allure.description('To click the respective module')
    def test_TC_09_event_vendor_tab(self):
        event_vendor = Event_vendor_tab(self.driver)
        time.sleep(4)
        event_vendor.Event_vendor_tab().click()
        time.sleep(4)

    @allure.description('To add and enter entire details of vendor')
    def test_TC_10_Add_new_vendor(self):
        add_vendor = Add_vendor(self.driver)
        time.sleep(3)
        add_vendor.Add_button().click()
        time.sleep(3)
        add_vendor.Title_click().click()
        time.sleep(3)
        add_vendor.Title_select().click()
        time.sleep(3)
        add_vendor.Firstname().send_keys('kelli4')
        time.sleep(3)
        add_vendor.Lastname().send_keys('tatey4')
        time.sleep(3)
        add_vendor.Companyname().send_keys('milton')
        time.sleep(3)
        add_vendor.Select_role_type().click()
        time.sleep(3)
        add_vendor.Type_click().click()
        time.sleep(3)
        add_vendor.Mailid().send_keys('kelli4tatey4@gmail.com')
        time.sleep(3)
        add_vendor.Mobileno().send_keys('9343948333')
        time.sleep(3)
        add_vendor.Website().send_keys('www.google.com')
        time.sleep(3)
        add_vendor.Assign_item_click().click()
        time.sleep(3)
        add_vendor.Assign_item_select().click()
        time.sleep(3)
        add_vendor.Assign_tags().send_keys('vendor')
        time.sleep(3)
        add_vendor.Address_tab().click()
        time.sleep(3)
        add_vendor.Search_address().send_keys('maiden')
        time.sleep(3)
        add_vendor.Country_name().send_keys('india')
        time.sleep(3)
        add_vendor.State_name().send_keys('tamilnadu')
        time.sleep(3)
        add_vendor.Suburb_name().send_keys('trichy')
        time.sleep(3)
        add_vendor.service_area_tab.click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/p-dropdown[1]/div[1]/div[3]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[@placeholder="Search Country"]').send_keys('IND')
        time.sleep(3)
        list1 = self.driver.find_elements_by_xpath('//div[@class="ui-dropdown-items-wrapper"]//ul//p-dropdownitem')
        i = -1
        for names in list1:
            i = i + 1
            country = names.text
            if country == "INDIA":
                self.driver.find_elements_by_xpath('//li[@class="ui-dropdown-item ui-corner-all"]//span')[i].click()
                time.sleep(7)
                break
        self.driver.find_element_by_xpath('//p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/p-dropdown[1]/div[1]/div[3]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[@placeholder="Search State"]').send_keys('TA')
        time.sleep(3)
        list3 = self.driver.find_elements_by_xpath('//div[@class="ui-dropdown-items-wrapper"]//ul//p-dropdownitem')
        k = -1
        for title3 in list3:
            k = k + 1
            state = title3.text
            if state == "TAMILNADU":
                self.driver.find_elements_by_xpath('//li[@class="ui-dropdown-item ui-corner-all"]//span')[k].click()
                time.sleep(7)
                break
        self.driver.find_element_by_xpath('//input[@placeholder="Enter Suburb"]').send_keys('trichy')
        time.sleep(3)
        self.driver.find_element_by_xpath('//a[contains(text(), "Social Link")]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/form[1]/div[1]/div[1]/div[1]/p-dropdown[1]/div[1]/div[3]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//div[@class="ui-dropdown-items-wrapper"]//ul//p-dropdownitem[3]//li//span').click()
        time.sleep(3)
        self.driver.find_element_by_id('txtMediaType').send_keys('www.twitter.com')
        time.sleep(3)
        self.driver.find_element_by_xpath('//a[contains(text(), "Bank Details")]').click()
        time.sleep(3)
        self.driver.find_element_by_id('txtAccountNo').send_keys('192329832')
        time.sleep(3)
        self.driver.find_element_by_id('txtAccountName').send_keys('kelly')
        time.sleep(3)
        self.driver.find_element_by_id('txtAccType').send_keys('savings')
        time.sleep(3)
        self.driver.find_element_by_id('txtBankName').send_keys('icici')
        time.sleep(3)
        self.driver.find_element_by_id('txtBranchName').send_keys('beachroad')
        time.sleep(3)
        self.driver.find_element_by_xpath('//a[contains(text(), "Other")]').click()
        time.sleep(3)
        self.driver.find_element_by_id('txtAlternateMobileNo').send_keys('9876543213')
        time.sleep(3)
        self.driver.find_element_by_id('txtAlternateMailID').send_keys('kellybob@gmail.com')
        time.sleep(3)
        self.driver.find_element_by_xpath('//button[@data-tour="savevendorVMdetails"]').click()
        time.sleep(3)

    @allure.description('To edit the details of vendor')
    def test_TC_11_edit_vendor(self):
        time.sleep(3)
        self.driver.find_element_by_xpath('//div[3]//table[1]//tbody[1]//tr[1]//td[8]//div[1]//a[1]').click()
        time.sleep(3)
        self.driver.find_element_by_id('txtBusinessName').send_keys('miltonx')
        time.sleep(3)
        self.driver.find_element_by_id('txtMailID').send_keys('robalberts@gmail.com')
        time.sleep(3)
        self.driver.find_element_by_id('txtMobileNo').send_keys('9343934333')
        time.sleep(3)
        self.driver.find_element_by_id('txtWebsite').send_keys('www.gmail.com')
        time.sleep(3)
        self.driver.find_element_by_xpath('//angular2-multiselect[1]/div[1]/div[1]/div[1]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//angular2-multiselect[1]/div[1]/div[2]/div[3]/div[3]/ul[1]/span[2]/li[1]/label[1]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[12]/div[1]/mat-chip-list[1]/div[1]/input[1]').send_keys('contracts')
        time.sleep(3)
        self.driver.find_element_by_xpath('//a[contains(text(), "Address")]').click()
        time.sleep(3)
        self.driver.find_element_by_id('txtAddress').send_keys('maid')
        time.sleep(3)
        self.driver.find_element_by_id('txtCountry').send_keys('us')
        time.sleep(3)
        self.driver.find_element_by_id('txtState').send_keys('ok')
        time.sleep(3)
        self.driver.find_element_by_id('txtSuburb').send_keys('tulsa')
        time.sleep(3)
        self.driver.find_element_by_xpath('//a[contains(text(), "Service Area")]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/p-dropdown[1]/div[1]/div[3]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[@placeholder="Search Country"]').send_keys('IND')
        time.sleep(3)
        lit1 = self.driver.find_elements_by_xpath('//div[@class="ui-dropdown-items-wrapper"]//ul//p-dropdownitem')
        m = -1
        for names1 in lit1:
            m = m + 1
            country2 = names1.text
            if country2 == "INDIA":
                self.driver.find_elements_by_xpath('//li[@class="ui-dropdown-item ui-corner-all"]//span')[m].click()
                time.sleep(7)
                break
        self.driver.find_element_by_xpath('//p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/p-dropdown[1]/div[1]/div[3]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[@placeholder="Search State"]').send_keys('TA')
        time.sleep(3)
        list6 = self.driver.find_elements_by_xpath('//div[@class="ui-dropdown-items-wrapper"]//ul//p-dropdownitem')
        n = -1
        for title4 in list6:
            n = n + 1
            state1 = title4.text
            if state1 == "TAMILNADU":
                self.driver.find_elements_by_xpath('//li[@class="ui-dropdown-item ui-corner-all"]//span')[n].click()
                time.sleep(7)
                break
        self.driver.find_element_by_xpath('//input[@placeholder="Enter Suburb"]').send_keys('trichy')
        time.sleep(3)
        self.driver.find_element_by_xpath('//a[contains(text(), "Social Link")]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/form[1]/div[1]/div[1]/div[1]/p-dropdown[1]/div[1]/div[3]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//div[@class="ui-dropdown-items-wrapper"]//ul//p-dropdownitem[3]//li//span').click()
        time.sleep(3)
        self.driver.find_element_by_id('txtMediaType').send_keys('www.twitter.com')
        time.sleep(3)
        self.driver.find_element_by_xpath('//a[contains(text(), "Bank Details")]').click()
        time.sleep(3)
        self.driver.find_element_by_id('txtAccountNo').send_keys('192339832')
        time.sleep(3)
        self.driver.find_element_by_id('txtAccountName').send_keys('kely')
        time.sleep(3)
        self.driver.find_element_by_id('txtAccType').send_keys('saving')
        time.sleep(3)
        self.driver.find_element_by_id('txtBankName').send_keys('icic')
        time.sleep(3)
        self.driver.find_element_by_id('txtBranchName').send_keys('beachroad')
        time.sleep(3)
        self.driver.find_element_by_xpath('//a[contains(text(), "Other")]').click()
        time.sleep(3)
        self.driver.find_element_by_id('txtAlternateMobileNo').send_keys('9876553213')
        time.sleep(3)
        self.driver.find_element_by_id('txtAlternateMailID').send_keys('kelybob@gmail.com')
        time.sleep(3)
        self.driver.find_element_by_xpath('//app-event-vendor-management[1]/app-addvendormodal[1]/div[2]/div[1]/div[1]/div[1]/div[1]').click()
        time.sleep(3)

    @allure.description('search the vendor in search text box and it will only show the vendor name related to text')
    def test_TC_12_search_vendor(self):
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[@placeholder="Search Vendor"]').send_keys('ryan')
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="search_vendor",
                      attachment_type=AttachmentType.PNG)
        time.sleep(3)
        self.driver.find_element_by_xpath('//a[@data-tour="searchvendoractionVM"]').click()
        time.sleep(3)
        search_names = self.driver.find_elements_by_xpath('//div[@class="tab-pane fade show active"]//div[1]//div[1]//div[3]//table[1]//tbody[1]//tr//td[2]')
        w = -1
        for o in search_names:
            w = w + 1
            names2 = o.text
            if names2 == "kelli2   tatey2":
                self.driver.find_elements_by_xpath('//td[@data-title="Action"]//div[1]//button')[o].click()
                time.sleep(3)
                break
        self.driver.find_element_by_xpath('//a[contains(text(), "Event Vendor")]').click()
        time.sleep(3)

    @allure.description('To delete the specific vendorww')
    def test_TC_13_delete_vendor(self):
        time.sleep(3)
        vendor_names = self.driver.find_elements_by_xpath('//div[3]//table[1]//tbody[1]//tr//td[2]')
        f = -1
        for s in vendor_names:
            f = f + 1
            names3 = s.text
            if names3 == "kelli4   tatey4":
                self.driver.find_elements_by_xpath('//td[@data-title="Action"]//div[1]//a[2]')[f].click()
                time.sleep(3)
                break
        self.driver.find_element_by_xpath('//button[contains(text(), "Yes, Remove it!")]').click()
        time.sleep(3)
        delete_vendor = self.driver.find_elements_by_xpath('//div[3]//table[1]//tbody[1]//tr//td[2]')
        x = -1
        for j in delete_vendor:
            x = x + 1
            names4 = j.text
            if names4 == "kelli3   tatey3":
                self.driver.find_elements_by_xpath('//td[@data-title="Action"]//div[1]//a[2]')[x].click()
                time.sleep(3)
                break
        self.driver.find_element_by_xpath('//button[contains(text(), "Yes, Remove it!")]').click()
        time.sleep(3)

        



































        








