import time
from datetime import date
import logging

logger = logging.getLogger('main_script')

# decorator to calculate duration
# taken by any function.
def calculate_time_console(func):
     
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
 
        # storing time before function execution
        begin = time.time()
         
        func(*args, **kwargs)
 
        # storing time after function execution
        end = time.time()
        print("Total time taken by : ", func.__name__, " is " , end - begin , " seconds")
 
    return inner1

def calculate_time_logger(func):
     
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
 
        # storing time before function execution
        begin = time.time()
         
        func(*args, **kwargs)
 
        # storing time after function execution
        end = time.time()
        logger.info("Total time taken by : " + str(func.__name__) + " is " + str(end - begin) + " seconds")
 
    return inner1

def get_date_stamp():
    today = date.today()
    return str(today)