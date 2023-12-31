import numpy as np
import config

def clip(x:float|np.ndarray)->float|np.ndarray:
    return x #np.clip(x,config.MIN_VALUE_NUMBER,config.MAX_VALUE_NUMBER)

from timeit import default_timer

def read_time_s()->int:
    return int(default_timer())