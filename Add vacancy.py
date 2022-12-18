import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestRecruitment_Candidates(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_e_add_vacancy(self):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.maximize_window()
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']" ).click()
        browser.find_element(By.XPATH, "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']/span[.='Recruitment']").click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/input').send_keys("Junior Quality Assurance")
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div/div[1]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div[2]/div[18]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div[1]/div/div[2]/div/div[1]/input').send_keys("Peter ")
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div[1]/div/div[2]/div/div[2]/div/span').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[7]/button[2]').click()
        browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()

        response_data = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]').text

        self.assertIn('Junior Quality Assurance', response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()