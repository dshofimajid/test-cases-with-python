import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_login_failed_wrong_password(self):
        browser = self.browser
        browser.get("https://katalon-demo-cura.herokuapp.com/")
        time.sleep(3)
        browser.find_element(By.ID,"menu-toggle").click()
        time.sleep(1)
        browser.find_element(By.LINK_TEXT, 'Login').click()
        time.sleep(1)
        browser.find_element(By.ID, 'txt-username').send_keys("John Doe")
        time.sleep(1)
        browser.find_element(By.ID, 'txt-password').send_keys("ThisIsAPassword")
        time.sleep(1)
        browser.find_element(By.ID, 'btn-login').click()

        response_message = browser.find_element(By.CLASS_NAME, "lead text-danger").text
        self.assertEqual(response_message, 'Login failed! Please ensure the username and password are valid.')

    def test_login_failed_wrong_username(self):
        browser = self.browser
        browser.get("https://katalon-demo-cura.herokuapp.com/")
        time.sleep(3)
        browser.find_element(By.ID,"menu-toggle").click()
        time.sleep(1)
        browser.find_element(By.LINK_TEXT, 'Login').click()
        time.sleep(1)
        browser.find_element(By.ID, 'txt-username').send_keys("dshofimajid")
        time.sleep(1)
        browser.find_element(By.ID, 'txt-password').send_keys("ThisIsNotAPassword")
        time.sleep(1)
        browser.find_element(By.ID, 'btn-login').click()

        response_message = browser.find_element(By.CLASS_NAME, "lead text-danger").text
        self.assertEqual(response_message, 'Login failed! Please ensure the username and password are valid.')

    def test_login_successful(self):
        browser = self.browser
        browser.get("https://katalon-demo-cura.herokuapp.com/")
        time.sleep(3)
        browser.find_element(By.ID,"menu-toggle").click()
        time.sleep(1)
        browser.find_element(By.LINK_TEXT, 'Login').click()
        time.sleep(1)
        browser.find_element(By.ID, 'txt-username').send_keys("John Doe")
        time.sleep(1)
        browser.find_element(By.ID, 'txt-password').send_keys("ThisIsNotAPassword")
        time.sleep(1)
        browser.find_element(By.ID, 'btn-login').click()

        response_message = browser.find_element(By.ID, "appointment").text
        self.assertEqual(response_message, 'Make Appointment')

    def test_make_appointment_failed_empty_date(self):
        browser = self.browser
        browser.get("https://katalon-demo-cura.herokuapp.com/")
        time.sleep(3)
        browser.find_element(By.ID,"menu-toggle").click()
        time.sleep(1)
        browser.find_element(By.LINK_TEXT, 'Login').click()
        time.sleep(1)
        browser.find_element(By.ID, 'txt-username').send_keys("John Doe")
        time.sleep(1)
        browser.find_element(By.ID, 'txt-password').send_keys("ThisIsNotAPassword")
        time.sleep(1)
        browser.find_element(By.ID, 'btn-login').click()
        time.sleep(1)
        browser.find_element(By.ID, "combo_facility").click() #value = "Tokyo CURA Healthcare Center")
        time.sleep(1)
        browser.find_element(By.ID, "radio_program_medicaid").click()
        time.sleep(1)
        browser.find_element(By.ID,"btn-book-appointment").click()
        time.sleep(1)

        response_message = browser.find_element(By.CLASS_NAME, "datepicker datepicker-dropdown dropdown-menu datepicker-orient-right datepicker-orient-top").text
        self.assertEqual(response_message, 'Please fill out this Field') #visit date column

    def test_make_appointment_successful(self):
        browser = self.browser
        browser.get("https://katalon-demo-cura.herokuapp.com/")
        time.sleep(3)
        browser.find_element(By.ID,"menu-toggle").click()
        time.sleep(1)
        browser.find_element(By.LINK_TEXT, 'Login').click()
        time.sleep(1)
        browser.find_element(By.ID, 'txt-username').send_keys("John Doe")
        time.sleep(1)
        browser.find_element(By.ID, 'txt-password').send_keys("ThisIsNotAPassword")
        time.sleep(1)
        browser.find_element(By.ID, 'btn-login').click()
        time.sleep(1)
        browser.find_element(By.ID, "combo_facility").click() #value = "Tokyo CURA Healthcare Center")
        time.sleep(1)
        browser.find_element(By.ID, "radio_program_medicaid").click()
        time.sleep(1)
        browser.find_element(By.CLASS_NAME,"input-group date").send_keys("30/12/2022")
        time.sleep(1)
        browser.find_element(By.ID,"btn-book-appointment").click()
        time.sleep(1)

        response_message = browser.find_element(By.ID, "summary").text
        self.assertEqual(response_message, 'Appointment Confirmation')

        def tearDown(self):
            self.browser.close()

unittest.main()

