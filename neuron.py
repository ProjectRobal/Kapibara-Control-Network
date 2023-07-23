import numpy as np
from base.dotproduct import Product
from dotproducts.dotnumpy import NumpyDotProduct
from base.activation import Activation
from activation.linear import Linear


class Neuron:
    def __init__(self,input_size:int,activation:Activation=Linear,dot_product:Product=NumpyDotProduct):
        '''
        input_size - a size of input weights

        state - a current state of a network
        past_state - a past state used in recurrent calculation
        '''
        # additional weight for past output, used for recurrsion
        # initial random weights
        self.input_weights=np.random.random(input_size+1)
        self.state:float=0.0
        self.past_state:float=0.0
        self.dot_product=dot_product
        self.activation=activation

        # evaluation of neuron used for crossover and mutation 
        self.evaluation:float=0.0

    def fire(self,inputs:np.array)->float:
        self.state=self.activation(self.dot_product(self.input_weights,[*inputs,self.past_state]))
        self.past_state=self.state

        return self.state


    def input_size(self)->int:
        return len(self.input_weights)

    def reset(self):

        self.past_state=self.state
        self.state=0.0
        self.evaluation=0.0

    def clear(self):
        self.state=0.0
        self.past_state=0.0
        self.evaluation=0.0

    def setEvaluation(self,eval:float):
        self.evaluation=eval

    def applyEvaluation(self,eval:float):
        self.evaluation+=eval

    def getEvaluation(self)->float:
        return self.evaluation

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