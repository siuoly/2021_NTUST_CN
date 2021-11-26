#!/bin/python3.8

# ref: https://stackoverflow.com/questions/366682/how-to-limit-execution-time-of-a-function-call
import signal
from contextlib import contextmanager
from timeit import default_timer as timer

class TimeoutException(Exception): pass

@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

def long_function_call():
    while True:
        a = 1 + 1

# usage
if __name__ == "__main__" :
    try:
        with time_limit(2):
            start = timer()
            long_function_call()
    except TimeoutException as e:
        pass
        # print("Timed out!")

    print( timer() - start )



