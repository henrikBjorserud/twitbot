import compose_tweet
from timing import wait_randomly_or_wait_for_sunrise
import bot
import pickle
from time import sleep
import trends_api


def get_password():
    """Get pickled password and username"""
    with open("login.pickle", "rb") as f:
        login = pickle.load(f)

    username = login["username"]
    password = login["password"]
    return username, password


def main():

    pickled_file = "valda_saved_lines.pickle"
    username, password = get_password()
    t_bot = bot.TheBot(username, password)
    t_bot.setup_webdriver()
    t_bot.login_to_twitter()

    while True:
        trend_list = trends_api.get_trends()
        text_to_tweet = compose_tweet.compose(trend_list, pickled_file)
        t_bot.tweet_text(text_to_tweet)
        sleep(wait_randomly_or_wait_for_sunrise())


if __name__ == "__main__":
    main()
