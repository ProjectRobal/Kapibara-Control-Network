import numpy as np
import numpy.ma as ma
from base.dotproduct import Product
from dotproducts.dotnumpy import NumpyDotProduct
from base.activation import Activation
from activation.linear import Linear

import config


class Neuron:
    def __init__(self,input_size:int,output_size:int):
        '''
        input_size - a size of input weights
        output_size - a size of output weights

        state - a current state of a network
        '''
        # additional weight for past output, used for recurrsion
        # initial random weights
        self.input_weights=(np.random.random(input_size)-0.5)*10
        self.output_weights=(np.random.random(output_size)-0.5)*10
        self.state:float=0.0
        self.dot_product=config.DOT_PRODUCT
        # count in how many trials neuron has particpated
        self.trails=0

        # evaluation of neuron used for crossover and mutation 
        self.evaluation:float=0.0

    def fire(self,inputs:np.ndarray)->np.ndarray:

        self.state=self.dot_product(self.input_weights,inputs)

        return self.output_weights*self.state


    def input_size(self)->int:
        return len(self.input_weights)
    
    def output_size(self)->int:
        return len(self.output_weights)

    def reset(self):

        self.state=0.0
        self.evaluation=0.0
        self.trails=0.0

    def reinitialize(self):
        self.input_weights=(np.random.random(self.input_size())-0.5)*10
        self.output_weights=(np.random.random(self.output_size())-0.5)*10

    def setEvaluation(self,eval:float):
        self.evaluation=eval

    def applyEvaluation(self,eval:float):
        self.evaluation+=eval
        self.trails+=1

    def getEvaluation(self)->float:
        return self.evaluation
    
    def Breedable(self)->bool:
        '''
            Whether the neuron is ready for breeding
        '''
        if self.trails>=config.NUMBER_OF_TRIALS:
            self.trails=0
            return True
        
        return False

    def Dump(self)->bytearray:
        '''
            Function used for neuron serialization,
            helpful for model saving
        '''
        pass

    def Load(self,data:bytearray):
        '''
            Function used for neuron deserialization,
            helpful for model loading
        '''
        pass        
    