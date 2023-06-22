####################
# Name:event vendor module
# Description: To do some operation
# Author: Alex herbert
# Date: 23-05-2022
####################
# Library use #
import time
import allure
import pyautogui
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.Clear_information import Clear_information
from PageObject.Delete_vendor import Delete_vendor
from PageObject.Edit_vendor import Edit_vendor
from PageObject.Popupwindow import Popupwindow
from PageObject.Search_vendor import Search_vendor
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
        time.sleep(4)
        add_vendor.Suburb_name().send_keys('trichy')
        time.sleep(3)
        add_vendor.Service_area_tab().click()
        time.sleep(3)
        add_vendor.Select_country().click()
        time.sleep(3)
        add_vendor.Search_country().send_keys('IND')
        time.sleep(3)
        list1 = add_vendor.Country_list()
        i = -1
        for names in list1:
            i = i + 1
            country = names.text
            if country == "INDIA":
                add_vendor.Element_list()[i].click()
                time.sleep(7)
                break
        add_vendor.Select_state().click()
        time.sleep(3)
        add_vendor.Search_state().send_keys('TA')
        time.sleep(3)
        list3 = add_vendor.State_list()
        k = -1
        for title3 in list3:
            k = k + 1
            state = title3.text
            if state == "TAMILNADU":
                add_vendor.State_element_list()[k].click()
                time.sleep(7)
                break
        add_vendor.Suburb_name1().send_keys('trichy')
        time.sleep(3)
        add_vendor.Social_link_tab().click()
        time.sleep(3)
        add_vendor.Select_social_media().click()
        time.sleep(3)
        add_vendor.Select_social_type().click()
        time.sleep(3)
        add_vendor.Link_text_box().send_keys('www.twitter.com')
        time.sleep(3)
        add_vendor.Add_link_button().click()
        time.sleep(3)
        add_vendor.Bank_details_tab().click()
        time.sleep(3)
        add_vendor.Account_no().send_keys('192329832')
        time.sleep(3)
        add_vendor.Account_name().send_keys('kelly')
        time.sleep(3)
        add_vendor.Account_type().send_keys('savings')
        time.sleep(3)
        add_vendor.Bank_name().send_keys('icici')
        time.sleep(3)
        add_vendor.Branch_name().send_keys('beachroad')
        time.sleep(3)
        add_vendor.Others_tab().click()
        time.sleep(3)
        add_vendor.Alternate_mobile_no().send_keys('9876543213')
        time.sleep(3)
        add_vendor.Alternate_email_id().send_keys('kellybob@gmail.com')
        time.sleep(3)
        #add_vendor.Save_detail_button().click()
        add_vendor.Close_button().click()
        time.sleep(3)

    @allure.description('To edit the details of vendor')
    def test_TC_11_edit_vendor(self):
        editvendor = Edit_vendor(self.driver)
        time.sleep(3)
        editvendor.Detail_button().click()
        time.sleep(4)
        editvendor.Edit_button().click()
        time.sleep(3)
        editvendor.Business_name().clear()
        editvendor.Business_name().send_keys('miltonx')
        time.sleep(3)
        #editvendor.Mail_id().send_keys('robalberts@gmail.com')
        #time.sleep(3)
        editvendor.Mobile_no().clear()
        editvendor.Mobile_no().send_keys('9343934333')
        time.sleep(3)
        editvendor.Website().clear()
        editvendor.Website().send_keys('www.gmail.com')
        time.sleep(3)
        editvendor.Assign_item().click()
        time.sleep(3)
        editvendor.Assign_item_checkbox_click().click()
        time.sleep(3)
        editvendor.Assign_tags().send_keys('contracts')
        time.sleep(3)
        editvendor.Address_tab().click()
        time.sleep(3)
        editvendor.Search_address().clear()
        editvendor.Search_address().send_keys('maid')
        time.sleep(3)
        editvendor.Country_name().clear()
        editvendor.Country_name().send_keys('us')
        time.sleep(3)
        editvendor.State_name().clear()
        editvendor.State_name().send_keys('ok')
        time.sleep(3)
        editvendor.Suburb_name().clear()
        editvendor.Suburb_name().send_keys('tulsa')
        time.sleep(3)
        editvendor.Service_area_tab().click()
        time.sleep(3)
        editvendor.Select_country().click()
        time.sleep(3)
        editvendor.Search_country().send_keys('IND')
        time.sleep(3)
        lit1 = editvendor.Country_list()
        m = -1
        for names1 in lit1:
            m = m + 1
            country2 = names1.text
            if country2 == "INDIA":
                editvendor.Country_select()[m].click()
                time.sleep(7)
                break
        editvendor.Select_state().click()
        time.sleep(3)
        editvendor.Search_state().send_keys('TA')
        time.sleep(3)
        list6 = editvendor.State_list()
        n = -1
        for title4 in list6:
            n = n + 1
            state1 = title4.text
            if state1 == "TAMILNADU":
                editvendor.State_select()[n].click()
                time.sleep(7)
                break
        time.sleep(3)
        editvendor.Enter_suburb().send_keys('trichy')
        time.sleep(3)
        editvendor.Social_link_tab().click()
        time.sleep(3)
        editvendor.Select_social_media_type().click()
        time.sleep(3)
        editvendor.Select_social_type().click()
        time.sleep(3)
        editvendor.Enter_social_media().send_keys('www.twitter.com')
        time.sleep(3)
        editvendor.Add_social_media_button().click()
        time.sleep(3)
        editvendor.Bank_details_tab().click()
        time.sleep(3)
        editvendor.Account_no().send_keys('192339832')
        time.sleep(3)
        editvendor.Account_name().send_keys('kely')
        time.sleep(3)
        editvendor.Account_type().send_keys('saving')
        time.sleep(3)
        editvendor.Bank_name().send_keys('icic')
        time.sleep(3)
        editvendor.Branch_name().send_keys('beachroad')
        time.sleep(3)
        editvendor.Other_tab().click()
        time.sleep(3)
        editvendor.Alternate_mobile_no().send_keys('9876553213')
        time.sleep(3)
        editvendor.Alternate_email_id().send_keys('kelybob@gmail.com')
        time.sleep(3)
        editvendor.Update_button().click()
        time.sleep(7)
        editvendor.Vendor_profile_image().click()
        time.sleep(3)
        editvendor.Click_to_upload().click()
        time.sleep(15)
        pyautogui.write(r"E:\Automation\profile_pic.jpg")  # path of File
        time.sleep(15)
        pyautogui.press('enter')
        time.sleep(15)
        editvendor.Message_tab().click()
        time.sleep(3)
        editvendor.Send_message_button().click()
        time.sleep(3)
        editvendor.Toclick().click()
        time.sleep(3)
        editvendor.Mailidselect().click()
        time.sleep(3)
        editvendor.Toclose().click()
        time.sleep(3)
        editvendor.Subject().send_keys('testing')
        time.sleep(3)
        editvendor.Entityclick().click()
        time.sleep(3)
        editvendor.Entityselect().click()
        time.sleep(3)
        ele = editvendor.Switch_to_frame()
        self.driver.switch_to.frame(ele)
        time.sleep(3)
        editvendor.Body_text().send_keys('test')
        time.sleep(3)
        self.driver.switch_to.default_content()
        time.sleep(8)
        allure.attach(self.driver.get_screenshot_as_png(), name="compose_mail_screenshot",
                      attachment_type=AttachmentType.PNG)
        time.sleep(3)
        editvendor.Send_key1().click()
        time.sleep(3)
        editvendor.Files_tab().click()
        time.sleep(3)
        editvendor.Attach_file_button().click()
        time.sleep(3)
        editvendor.Attach_from_computer().click()
        time.sleep(3)
        editvendor.Click_to_file_upload().click()
        time.sleep(3)
        pyautogui.write(r"E:\Automation\Contact.xls")  # path of File
        time.sleep(15)
        pyautogui.press('enter')
        time.sleep(20)
        editvendor.Notes_tab().click()
        time.sleep(3)
        editvendor.Add_notes().click()
        time.sleep(3)
        editvendor.Add_notes_text_box().send_keys("test")
        time.sleep(3)
        editvendor.Back_button().click()
        time.sleep(3)


    @allure.description('search the vendor in search text box and it will only show the vendor name related to text')
    def test_TC_12_search_vendor(self):
        searchvendor = Search_vendor(self.driver)
        time.sleep(3)
        searchvendor.Search_vendor_textbox().send_keys('ryan')
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="search_vendor",
                      attachment_type=AttachmentType.PNG)
        time.sleep(3)
        searchvendor.Search_vendor_tab().click()
        time.sleep(3)
        search_names = searchvendor.Vendor_name_list()
        w = -1
        for o in search_names:
            w = w + 1
            names2 = o.text
            if names2 == "kelli4 tatey4":
                searchvendor.Vendor_name()[w].click()
                time.sleep(3)
                break
        searchvendor.Event_vendor_tab().click()
        time.sleep(5)

    @allure.description('To delete the specific vendor')
    def test_TC_13_delete_vendor(self):
        deletevendor = Delete_vendor(self.driver)
        time.sleep(7)
        #vendor_names = deletevendor.Vendor_name()
        #f = -1
        #for s in vendor_names:
        #    f = f + 1
        #    names3 = s.text
        #    if names3 == "kelli4 tatey4":
        #        deletevendor.Vendor_delete()[f].click()
        #        time.sleep(3)
        #        break
        #deletevendor.Confim_delete().click()
        #time.sleep(3)
        #delete_vendor = deletevendor.Vendor_name1()
        #x = -1
        #for j in delete_vendor:
        #    x = x + 1
        #    names4 = j.text
        #    if names4 == "kelli4 tatey4":
        #        deletevendor.Vendor_delete1()[x].click()
        #        time.sleep(3)
        #        break
        #time.sleep(3)
        #deletevendor.Confim_delete().click()
        #time.sleep(3)
        deletevendor.Vendor_delete4().click()
        time.sleep(3)
        deletevendor.Confim_delete().click()
        time.sleep(3)

    def test_TC_14_clear_information(self):
        clearinformation = Clear_information(self.driver)
        time.sleep(3)
        clearinformation.Detail_button().click()
        time.sleep(4)
        clearinformation.Edit_button().click()
        time.sleep(3)
        clearinformation.Business_name().clear()
        time.sleep(3)
        # editvendor.Mail_id().send_keys('robalberts@gmail.com')
        # time.sleep(3)
        clearinformation.Mobile_no().clear()
        time.sleep(3)
        clearinformation.Website().clear()
        time.sleep(3)
        clearinformation.Assign_item().click()
        time.sleep(3)
        clearinformation.Address_tab().click()
        time.sleep(3)
        clearinformation.Search_address().clear()
        time.sleep(3)
        clearinformation.Country_name().clear()
        time.sleep(3)
        clearinformation.State_name().clear()
        time.sleep(3)
        clearinformation.Suburb_name().clear()
        time.sleep(3)
        clearinformation.Service_area_tab().click()
        time.sleep(3)
        clearinformation.Clear_suburb().click()
        time.sleep(3)
        clearinformation.Social_link_tab().click()
        time.sleep(3)
        clearinformation.Clear_social_link().click()
        time.sleep(3)
        clearinformation.Bank_details_tab().click()
        time.sleep(3)
        clearinformation.Account_no().clear()
        time.sleep(3)
        clearinformation.Account_name().clear()
        time.sleep(3)
        clearinformation.Account_type().clear()
        time.sleep(3)
        clearinformation.Bank_name().clear()
        time.sleep(3)
        clearinformation.Branch_name().clear()
        time.sleep(3)
        clearinformation.Other_tab().click()
        time.sleep(3)
        clearinformation.Alternate_mobile_no().clear()
        time.sleep(3)
        clearinformation.Alternate_email_id().clear()
        time.sleep(3)
        clearinformation.Update_button().click()
        time.sleep(7)
        clearinformation.Clear_profile_image().click()
        time.sleep(3)
        clearinformation.Files_tab().click()
        time.sleep(3)
        clearinformation.File_delete().click()
        time.sleep(3)
        clearinformation.Confirm_delete().click()
        time.sleep(3)
        clearinformation.Notes_tab().click()
        time.sleep(3)
        clearinformation.Delete_note().click()
        time.sleep(3)
        clearinformation.Confirm_delete().click()
        time.sleep(3)
        clearinformation.Back_button().click()
        time.sleep(3)

        



































        








