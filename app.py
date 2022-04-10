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
    print(username, password)
    tweet = compose_tweet.compose()
    print(tweet)
    t_bot = bot.TheBot(username, password)
    print(t_bot)
    sleep(5)
    t_bot.setup_webdriver()
    print(t_bot)
    sleep(5)
    t_bot.login_to_twitter()
    print("hello2")
    sleep(5)
    t_bot.tweet_text(tweet)
    print("hello3")



if __name__ == '__main__':
    main()
