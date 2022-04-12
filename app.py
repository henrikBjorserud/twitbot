import compose_tweet
import bot
import pickle
from time import sleep


def get_password():
    '''Get pickled password and username'''
    with open('login.pickle', 'rb') as f:
        login = pickle.load(f)

    username = login['username']
    password = login['password']
    return username, password


def main():

    username, password = get_password()
    tweet = compose_tweet.compose()
    print(tweet)
    t_bot = bot.TheBot(username, password)
    t_bot.setup_webdriver()
    t_bot.login_to_twitter()
    t_bot.tweet_text(tweet)


if __name__ == '__main__':
    main()
