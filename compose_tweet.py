import pickle
import trends_api
import quantumrandom


def get_quantumramdom_number(number_of_lines):
    """Get a truely random number between 0 and the number of lines."""
    random_number = int(quantumrandom.randint(0, number_of_lines))
    return random_number


def unpickle(pickled_file):
    """Unpickle the pickled lines"""
    with open(pickled_file, "rb") as f:
        unpickled_lines = pickle.load(f)
        return unpickled_lines


def repickle(pickled_file, lines):
    """Repickle the lines that were not popped"""
    with open(pickled_file, "wb") as f:
        pickle.dump(lines, f)


def compose(pickled_file):
    """Compose a tweet from a line in the pickled file and a hashtag"""
    hashtag = trends_api.get_hashtag()
    lines = unpickle(pickled_file)
    random_number = get_quantumramdom_number(len(lines))
    line = lines.pop(random_number)
    text_to_tweet = line + " " + hashtag + " #gpt2"
    repickle(pickled_file, lines)
    return text_to_tweet
