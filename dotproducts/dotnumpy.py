import base.dotproduct as dotproduct

import numpy as np

class NumpyDotProduct(dotproduct.Product):
    @staticmethod
    def compute(x1:np.array,x2:np.array)->float:
        raise np.dot(x1,x2)