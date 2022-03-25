import pickle
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


DRIVER = None
WAIT = None


def get_password():
    '''Get pickled password and username'''
    with open('login.pickle', 'rb') as f:
        login = pickle.load(f)

    username = login['username']
    password = login['password']
    return username, password


#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--window-size=1420,1080')
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-software-rasterizer')


def setup_webdriver():
    '''Setup webdriver, download chromedriver'''
    global DRIVER
    global WAIT
    # options = Options()
    # options.add_argument("disable-gpu")

    DRIVER = webdriver.Chrome(
            service=Service(
                ChromeDriverManager(
                    chrome_type=ChromeType.CHROMIUM).install()))
   # Set wait
    WAIT = WebDriverWait(DRIVER, 10)



def login_twitter():
    '''Login to twitter account'''

    tweeter_url = "https://twitter.com/login"
    DRIVER.get(tweeter_url)

    # Get username and password
    username, password = get_password()

    # Input username
    username_input = WAIT.until(ec.visibility_of_element_located((By.NAME,
        "session[username_or_email]")))
    username_input.send_keys(username)

    # Input password
    password_input = WAIT.until(ec.visibility_of_element_located((By.NAME,
        "session[password]")))
    password_input.send_keys(password)

    # Push login button
    login_button = WAIT.until(ec.visibility_of_element_located((By.XPATH,
        "//div[@data-testid='LoginForm_Login_Button']")))
    login_button.click()


def tweet_text(text):
    ''' Make a tweet '''
    # Find text span
    tweet_text_span = DRIVER.find_element_by_xpath(
            "//div[@data-testid='tweetTextarea_0']/div/div/div/span")

    # Input text
    tweet_text_span.send_keys(text)


    # Locate button
    tweet_button = WAIT.until(ec.visibility_of_element_located((
        By.XPATH,"//div[@data-testid='tweetButtonInline']")))


    # Push button
    tweet_button.click()
