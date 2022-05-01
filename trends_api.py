from pytrends.request import TrendReq
from random import randint
import pickle

PYTRENDS = TrendReq()

def sports_removal(trend_list):
    """Check if trend is present in list of sports."""
    with open("sports.pickle", "rb") as f:
            sports = pickle.load(f)
    non_sport_trends = [trend for trend in trend_list if trend not in sports]
    return non_sport_trends


def get_trends():
    """Get the hottest trends in Sweden right now"""
    trends = PYTRENDS.trending_searches(pn="sweden")
    trend_list = [trends.loc[i][0] for i in range(len(trends))]
    return trend_list


def parse_hashtag(trend_list):
    """Get trends and return a random one"""
    non_sport_trends = sports_removal(trend_list)
    trend = trend_list[randint(0, len(non_sport_trends))]
    trend = trend.replace(" ", "")
    trend = ''.join(filter(str.isalnum, trend))
    trend = trend.lstrip("1234567890")
    trend = f"#{trend}"
    
    return trend
