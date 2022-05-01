from compose_tweet import *
import time
from trends_api import *


def test_unpickle():
    test_lines = unpickle("test_lines.pickle")
    assert type(test_lines) is list


def test_quantum_random():
    test_lines = unpickle("test_lines.pickle")
    n_o_l = len(test_lines)
    assert type(get_quantum_random_number(n_o_l)) is int



# def test_get_trends():
#     trends = get_trends()
#     assert type(trends) is list


def test_parse_hashtag():
    trend_list = ['1waffles23', '$fishes', 'TrEMoLo**', 'leek', 'Älårö', 'trendsds', '!@#$%^&*()fd', 'swertz', 'Omni', 'RealMadrid', 'HV71']
    for hashtag in trend_list: 
        tag = parse_hashtag(trend_list)
    assert type(tag) is str


def test_compose():
    trend_list = ['1waffles23', '$fishes', 'TrEMoLo**', 'leek', 'Älårö', 'trendsds', '!@#$%^&*()fd', 'swertz', 'Omni', 'RealMadrid', 'HV71']
    pickled_file = "test_lines.pickle"
    text_to_tweet = compose(trend_list, pickled_file)
    print(text_to_tweet)
    assert type(text_to_tweet) is str
