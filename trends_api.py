from pytrends.request import TrendReq
from random import randint
import pickle

PYTRENDS = TrendReq()

def sports_removal(trend):
    """Check if trend is present in list of sports."""

    with open("sports.pickle", "rb") as f:
            sports = pickle.load(f)

    sports_check = any(word in trend for word in sports)

    return sports_check

def get_hashtag():
    """Get the hottest trends in Sweden right now and return a random one"""
    trends = PYTRENDS.trending_searches(pn="sweden")
    trend_list = [trends.loc[i][0] for i in range(len(trends))]
    trend = trend_list[randint(0, 10)]
    trend = trend.replace(" ", "")
    trend = trend.lstrip("1234567890")
    trend = f"#{trend}"
    
    return trend

