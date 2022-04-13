from pytrends.request import TrendReq
from random import randint

PYTRENDS = TrendReq()


def get_hashtag():
    """Get the hottest trends in Sweden right now and return a random one"""
    trends = PYTRENDS.trending_searches(pn="sweden")
    trend_list = [trends.loc[i][0] for i in range(len(trends))]
    trend = trend_list[randint(0, 10)]
    trend = trend.replace(" ", "")
    trend = f"#{trend}"
    return trend
