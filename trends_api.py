import pandas as pd
from pytrends.request import TrendReq

PYTRENDS = TrendReq()
from random import randint


def get_hashtag():
    trends = PYTRENDS.trending_searches(pn="sweden")
    trend_list = [trends.loc[i][0] for i in range(len(trends))]
    trend = trend_list[randint(0, 10)]
    trend = trend.replace(" ", "")
    trend = f"#{trend}"
    return trend
