import random
import time

BUFFER_TIME_MAX = 2
BUFFER_TIME_MIN = 0.001

def wait_random_buffer(min = BUFFER_TIME_MAX,
                       max = BUFFER_TIME_MIN,
                       tab_amount=""):
    """
    make the computer wait.
    this makes it seem like it's important

    :param min:
    :param max:
    :param tab_amount:
    :return:
    """
    #this is a random decimal between the min & max values
    random_buffer = random.uniform(min,max)
    #print(tab_amount,"random_buffer =", random_buffer)
    time.sleep(random_buffer)