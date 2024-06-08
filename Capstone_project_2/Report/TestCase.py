# Access the variables used or maintained by the Python
# Functions that interact strongly with the interpreter.
import sys
# Module provides a way of using operating system-dependent
# Functionality like reading or writing to the file system
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Data import data
from Locator import locator

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

import pytest


class TestCase:
    @pytest.fixture
    def start(self, request):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 5)
        self.driver.maximize_window()
        request.cls.driver = self.driver
        request.cls.wait = self.wait
        yield
        self.driver.quit()

    def login(self, username, password):
        """
        Method to log in using the provided username and password.
        """
        try:
            self.wait.until(EC.element_to_be_clickable((By.NAME, locator.WebSource().Username))).send_keys(username)
            self.wait.until(EC.element_to_be_clickable((By.NAME, locator.WebSource().Password))).send_keys(password)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().login_button))).click()
            print("Login successful")
        except Exception as e:
            pytest.fail(f"Login failed: {e}")

    def logout(self):
        """
        Method to log out from the webpage.
        """
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().userMenu))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().logout))).click()
            print("Logout successful")
        except Exception as e:
            pytest.fail(f"Logout failed: {e}")

    def provide_admin_access(self):
        """
        Method to provide admin password if access is requested.
        """
        try:
            admin_access = self.wait.until(EC.presence_of_element_located((By.XPATH, locator.WebSource().access)))
            if admin_access:
                self.driver.find_element(By.NAME, locator.WebSource().Password).send_keys("admin123")
                self.driver.find_element(By.XPATH, locator.WebSource().SubmitAccess).click()
                print("Admin password provided and access granted.")
        except TimeoutException:
            print("No access requested.")

    @pytest.mark.usefixtures("start")
    def test_TC_PIM_01(self):
        """
        Test Case ID: TC_PIM_01
        Test objective: Forgot Password link validation on login page
        """
        try:
            self.driver.get(data.TestData().url)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().forget_password))).click()
            self.wait.until(EC.element_to_be_clickable((By.NAME, locator.WebSource().Username))).send_keys("Admin")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().reset_button))).click()
            print("Reset Password link sent successfully")
            assert self.driver.current_url == data.TestData().password_reset_link
        except Exception as e:
            pytest.fail(f"Test failed: {e}")

    @pytest.mark.usefixtures("start")
    def test_TC_PIM_02(self):
        """
        Test Case ID: TC_PIM_02
        Test objective: Validate "Title" of the Page as "OrangeHRM"
                        Header Validation on Admin Page
        """
        self.driver.get(data.TestData().url)
        self.login("Admin", "admin123")
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Admin))).click()
            title = self.driver.title
            assert title == "OrangeHRM", "Title validation failed"

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().user_Management))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().users))).click()
            assert self.driver.current_url == data.TestData().UserManagement, "User Management page validation failed"

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Job))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Job_titles))).click()
            assert self.driver.current_url == data.TestData().JobTitles, "Job page validation failed"

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Organization))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().General_information))).click()
            assert self.driver.current_url == data.TestData().Organization, "Organization page validation failed"

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Qualifications))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Skills))).click()
            assert self.driver.current_url == data.TestData().Qualification, "Qualification page validation failed"

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Nationalities))).click()
            assert self.driver.current_url == data.TestData().nationality, "Nationalities page validation failed"

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Corporate_Banking))).click()
            assert self.driver.current_url == data.TestData().Corporate_Branding, ("Corporate Banking page "
                                                                                   "validation failed")

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Configuration))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Email_configuration))).click()
            assert self.driver.current_url == data.TestData().Configuration, "Configuration page validation failed"
        except Exception as e:
            pytest.fail(f"Test failed: {e}")
        finally:
            self.logout()

    @pytest.mark.usefixtures("start")
    def test_TC_PIM_03(self):
        """
        Test Case ID: TC_PIM_03
        Test objective: Main Menu Validation on Admin Page
        """
        self.driver.get(data.TestData().url)
        self.login("Admin", "admin123")
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Admin))).click()
            self.provide_admin_access()
            assert self.driver.current_url == data.TestData().Admin, "Admin page validation failed"

            pages = [
                (locator.WebSource().PIM, data.TestData().PIM),
                (locator.WebSource().Leave, data.TestData().Leave),
                (locator.WebSource().Time, data.TestData().Time),
                (locator.WebSource().Recruitment, data.TestData().Recruitment),
                (locator.WebSource().My_Info, data.TestData().MyInfo),
                (locator.WebSource().Performance, data.TestData().Performance),
                (locator.WebSource().Dashboard, data.TestData().Dashboard),
                (locator.WebSource().Directory, data.TestData().Directory),
                (locator.WebSource().Maintenance, data.TestData().Maintenance),
                (locator.WebSource().Buzz, data.TestData().Buzz)
            ]

            for page_locator, expected_url in pages:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, page_locator))).click()
                self.provide_admin_access()
                assert self.driver.current_url == expected_url, f"{expected_url} page validation failed"
        except Exception as e:
            pytest.fail(f"Test failed: {e}")
        finally:
            self.logout()
