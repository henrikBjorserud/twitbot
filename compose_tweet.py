import pickle
from random import randint
import trends_api
import quantumrandom

def compose():
    hashtag = trends_api.get_hashtag()
    lines = pickle.load(open("lines.pickle", "rb"))
    return lines[int(quantumrandom.randint(-1, len(lines)))] + " " + hashtag
