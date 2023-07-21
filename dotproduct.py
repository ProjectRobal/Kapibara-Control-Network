'''
    A file that store base class for dot product calculation for neurons.
'''

import numpy as np

class Product:
    @staticmethod
    def compute(x1:np.array,x2:np.array)->float:
        raise NotImplementedError()