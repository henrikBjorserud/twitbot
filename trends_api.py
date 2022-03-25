import pandas as pd
from pytrends.request import TrendReq
PYTRENDS = TrendReq()


def get_two_hashtags():
trends = PYTRENDS.trending_searches(pn='sweden')

trend_list = [trends.loc[i][0] for i in range(len(trends))]


