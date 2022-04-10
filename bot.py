from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


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
        chrome_options.add_argument('--user-data-dir=/home/henrik/Desktop/temp')
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
        

        self.driver.get("https://twitter.com/login")

        # Input username
        username_input = self.wait.until(
            ec.visibility_of_element_located((By.NAME, "session[username_or_email]"))
        )
        username_input.send_keys(self.username)

        # Input password
        password_input = self.wait.until(
            ec.visibility_of_element_located((By.NAME, "session[password]"))
        )
        password_input.send_keys(self.password)

        # Push login button
        login_button = self.wait.until(
            ec.visibility_of_element_located(
                (By.XPATH, "//div[@data-testid='LoginForm_Login_Button']")
            )
        )
        login_button.click()


    def tweet_text(self, text):
        """Make a tweet"""
        # Find text span
        tweet_text_span = self.driver.find_element_by_xpath(
            "//div[@data-testid='tweetTextarea_0']/div/div/div/span"
        )

        # Input text
        tweet_text_span.send_keys(text)

        # Locate button
        tweet_button = self.wait.until(
            ec.visibility_of_element_located(
                (By.XPATH, "//div[@data-testid='tweetButtonInline']")
            )
        )

        # Push button
        tweet_button.click()
