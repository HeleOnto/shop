import random
import string
from datetime import date


def generate_ref_code():
    date_str = date.today().strftime('%d%m%Y')
    rand_str = "-" + "".join([random.choice(string.ascii_uppercase) for count in range(3)])
    return date_str + rand_str
