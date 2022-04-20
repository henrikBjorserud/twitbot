import compose_tweet
from timing import wait_randomly_or_wait_for_sunrise
import bot
import pickle
from time import sleep


def get_password():
    '''Get pickled password and username'''
    with open("login.pickle", "rb") as f:
        login = pickle.load(f)

    username = login["username"]
    password = login["password"]
    return username, password


def login_and_setup():
    '''Make the bot post stuff'''
    username, password = get_password()
    tweet = compose_tweet.compose()
    print(tweet)
    t_bot = bot.TheBot(username, password)
    t_bot.setup_webdriver()
    t_bot.login_to_twitter()
    t_bot.tweet_text(tweet)


def main():

    username, password = get_password()
    t_bot = bot.TheBot(username, password)
    t_bot.setup_webdriver()
    t_bot.login_to_twitter()
    
    while True:
        tweet = compose_tweet.compose()
        t_bot.tweet_text(tweet)        
        sleep(wait_randomly_or_wait_for_sunrise())


if __name__ == "__main__":
    main()
