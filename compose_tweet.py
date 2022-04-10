import pickle
from random import randint
import trends_api
import quantumrandom


def compose():
    """Compose a tweet from a line in the pickled file and a hashtag"""
    hashtag = trends_api.get_hashtag()
    with open("lines.pickle", "rb") as f:
        lines = pickle.load(f)
    random_number = int(quantumrandom.randint(0, len(lines)))
    line = lines.pop(random_number)
    tweet = line + " " + hashtag
    repickle(lines)
    return tweet


def repickle(lines):
    """Repickle the lines that were not popped"""

    with open("lines.pickle", "wb") as f:
        pickle.dump(lines, f)
