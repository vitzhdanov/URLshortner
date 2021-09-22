import random
import string


def random_url():
    return ''.join(random.sample(string.ascii_letters, 5))
