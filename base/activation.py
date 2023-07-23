'''
    A base class for activation function for neurons.
'''

from typing import Any


class Activation:
    @staticmethod
    def activate(x:float)->float:
        raise NotImplementedError()
    
    def __call__(self, x:float) -> float:
        return self.activate(x)