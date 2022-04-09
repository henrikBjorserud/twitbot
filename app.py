import compose_tweet


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
    bot = TheBot(username, password)
    bot .


    
    


if __name__ == '__main__':
    main()
