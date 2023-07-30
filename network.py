import numpy as np
import numpy.ma as ma
import random

from base.activation import Activation
from base.dotproduct import Product
from activation.linear import Linear
from dotproducts.dotnumpy import NumpyDotProduct
import neuron
    

class Network:
    pass
    '''
        A class that defines network schematic.
        It stores layers wich defines hidden layers of network.
        And information of number of layers and total count of neurons.
        Each layer will have neuron count equal to tau.
    '''
    def __init__(self,input_size:int,output_size:int,theta:int,tau:int,max_neuron_weight_size:int,dotproduct:Product=NumpyDotProduct):
        pass