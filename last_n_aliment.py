import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        with open('output.txt', 'wt') as f:
            print(func.__name__, end-start, file=f)
        return result
    return wrapper

@timethis
def countdown(n : int):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1

if __name__ == "__main__":
    countdown(1000000)