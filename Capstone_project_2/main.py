from Data import data
from Locator import locator
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class TestCase:

    def __init__(self):
        """
        Constructor method that initializes the class instance.
        It sets up URLs, initializes the WebDriver, and WebDriverWait.
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 5)
        self.action = ActionChains(self.driver)

    def start(self):
        """
        Method to start the WebDriver, navigate to the provided URL, and maximize the window.
        """
        self.driver.get(data.TestData().url)
        self.driver.maximize_window()
        self.wait.until(EC.url_to_be(data.TestData().url))

    def close(self):
        """
        Method to quit the WebDriver, closing the browser window.
        """
        self.driver.quit()

    def login(self, username, password):
        """
        Method to logging in using the provided username and password.
        """
        try:
            self.start()
            # Enter the username
            self.wait.until(EC.element_to_be_clickable((By.NAME, locator.WebSource().Username))).send_keys(username)
            # Enter the password
            self.wait.until(EC.element_to_be_clickable((By.NAME, locator.WebSource().Password))).send_keys(password)
            # Click login button
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().login_button))).click()
            print("Login successful")
        except Exception as e:
            print("Login failed:", e)

    def logout(self):
        """
        Method to log out from the webpage.
        """
        try:
            # user menu
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().userMenu))).click()
            # Log out
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().logout))).click()
            print("Logout successful")
        except Exception as e:
            print("Logout failed:", e)

    def access(self):
        """
        Method to provide admin password if access is requested.
        """
        try:
            # Check if the banner is present
            administrator_access = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, locator.WebSource().access)))
            if administrator_access:
                self.driver.find_element(By.NAME, locator.WebSource().Password).send_keys("admin123")
                self.driver.find_element(By.XPATH, locator.WebSource().SubmitAccess).click()
                print("Admin password provided and access granted.")
        except TimeoutException:
            print("No access requested.")

    def TC_PIM_01(self):
        """
        Test Case ID: TC_PIM_01
        Test objective: Forgot Password link validation on login page
        """
        try:
            self.start()
            # Click on forget Password
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().forget_password))).click()
            # Enter the username as Admin
            self.wait.until(EC.element_to_be_clickable((By.NAME, locator.WebSource().Username))).send_keys("Admin")
            # Click on submit to get the reset link
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().reset_button))).click()
            print("Reset Password link sent successfully ")
            print("Password reset link url:", self.driver.current_url)
        except Exception as e:
            print("Test failed:", e)

    def TC_PIM_02(self):
        """
        Test Case ID: TC_PIM_02
        Test objective: Validate "Title" of the Page as "OrangeHRM"
                        Header Validation on Admin Page
        """
        self.start()
        self.login("Admin", "admin123")
        # Enter the Admin page
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().title))).click()
        # verify the title of the page
        title = self.driver.title
        if title == "OrangeHRM":
            print("Title page validation is successful")
        else:
            print("Title validation failed")

        try:
            # Navigate to Admin page
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Admin))).click()

            # User Management page option
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().user_Management))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().users))).click()
            if self.driver.current_url == data.TestData().UserManagement:
                print("User Management Page is validated successfully")
            else:
                print("User Management page validation failed")

            # Job page options
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Job))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Job_titles))).click()
            if self.driver.current_url == data.TestData().JobTitles:
                print("Job Page is validated successfully")
            else:
                print("Job page validation failed")

            # Organization page options
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Organization))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().General_information))).click()
            if self.driver.current_url == data.TestData().Organization:
                print("Organization page is validated successfully")
            else:
                print("Organization page validation failed")

            # Qualification page options
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Qualifications))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Skills))).click()
            if self.driver.current_url == data.TestData().Qualification:
                print("Qualification page is validated successfully")
            else:
                print("Qualification page validation failed")

            # Nationalities page options
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Nationalities))).click()
            if self.driver.current_url == data.TestData().nationality:
                print("Nationalities page is validated successfully")
            else:
                print("Nationalities page validation failed")

            # Corporate page options
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Corporate_Banking))).click()
            if self.driver.current_url == data.TestData().Corporate_Branding:
                print("Corporate Banking page is validated successfully")
            else:
                print("Corporate Banking page validation failed")

            # Configuration page options
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Configuration))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Email_configuration))).click()
            if self.driver.current_url == data.TestData().Configuration:
                print("Configuration page is validated successfully")
            else:
                print("Configuration page validation failed")

        except Exception as e:
            print("Test failed:", e)
        finally:
            self.logout()

    def TC_PIM_03(self):
        """
        Test Case ID: TC_PIM_03
        Test objective: Main Menu Validation on Admin Page
        """
        try:
            self.start()
            self.login("Admin", "admin123")

            # Main menu validation
            # Admin page
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Admin))).click()
            self.access()
            if self.driver.current_url == data.TestData().Admin:
                print("Admin page validated successfully")
            else:
                print("Admin page validation failed")

            # PIM page
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().PIM))).click()
            self.access()
            if self.driver.current_url == data.TestData().PIM:
                print("PIM page validated successfully")
            else:
                print("PIM page validation failed")

            # Leave page
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Leave))).click()
            self.access()
            if self.driver.current_url == data.TestData().Leave:
                print("Leave page validated successfully")
            else:
                print("Leave page validation failed")

            # Time page
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Time))).click()
            self.access()
            if self.driver.current_url == data.TestData().Time:
                print("Time page validated successfully")
            else:
                print("Time page validation failed")

            # Recruitment page
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Recruitment))).click()
            self.access()
            if self.driver.current_url == data.TestData().Recruitment:
                print("Recruitment page validated successfully")
            else:
                print("Recruitment page validation failed")

            # My info page
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().My_Info))).click()
            self.access()
            if self.driver.current_url == data.TestData().MyInfo:
                print("My info page validated successfully")
            else:
                print("My info page validation failed")

            # Performance page
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Performance))).click()
            if self.driver.current_url == data.TestData().Performance:
                print("Performance page validated successfully")
            else:
                print("Performance page validation failed")

            # Dashboard page
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Dashboard))).click()
            self.access()
            if self.driver.current_url == data.TestData().Dashboard:
                print("Dashboard page validated successfully")
            else:
                print("Dashboard page validation failed")

            # Directory page
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Directory))).click()
            self.access()
            if self.driver.current_url == data.TestData().Directory:
                print("Directory page validated successfully")
            else:
                print("Directory page validation failed")

            # Maintenance page
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Maintenance))).click()
            self.access()
            if self.driver.current_url == data.TestData().Maintenance:
                print("Maintenance page validated successfully")
            else:
                print("Maintenance page validation failed")

            # Buzz page
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.WebSource().Buzz))).click()
            self.access()
            if self.driver.current_url == data.TestData().Buzz:
                print("Buzz page validated successfully")
            else:
                print("Buzz page validation failed")

        except Exception as e:
            print("Test failed:", e)
        finally:
            self.close()


# Usage
obj = TestCase()
obj.TC_PIM_01()
obj.TC_PIM_02()
obj.TC_PIM_03()
