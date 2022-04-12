from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from time import sleep


class TheBot:

    def __init__(self, username, password):

        self.driver = None
        self.wait = None
        self.username = username
        self.password = password

    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--window-size=1420,1080')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-software-rasterizer')


    def setup_webdriver(self):
        """Setup webdriver, download chromedriver"""

        chrome_options = Options()
        chrome_options.add_argument('--user-data-dir=/home/plejd/Desktop/temp')
        chrome_options.add_argument('--remote-debugging-port-9222')
        self.driver = webdriver.Chrome(options = chrome_options,
            service=Service(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            )
        )
        #  Set wait
        self.wait = WebDriverWait(self.driver, 10)


    def login_to_twitter(self):
        """Login to twitter account"""
        driver = self.driver
        username = self.username
        password = self.password
        wait = self.wait

        driver.get("https://twitter.com/login")


        """
        username_field = wait.until(
            ec.visibility_of_element_located(
                (By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
            )
        )
        username_field.send_keys(username)
        
        next_button = wait.until(
            ec.element_to_be_clickable(
                (By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]')
            )
        )
        next_button.click()
        
        password_field = wait.until(
            ec.visibility_of_element_located(
                (By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            )
        )
        password_field.send_keys(password)
                 
        
        login_button = wait.until(
            ec.element_to_be_clickable(
                (By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div')
            )
        )
        login_button.click()
        """

    def tweet_text(self, text):
        """Make a tweet"""

        wait = self.wait
        driver = self.driver
       
        login_button = wait.until(
            ec.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
            )
        )
        login_button.click()       



        tweet_field = wait.until(
            ec.visibility_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
            )
        )
        tweet_field.send_keys(text)

        # Locate button
        
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB * 8, Keys.RETURN)
        actions.perform()

        # Push button 
        sleep(5)
