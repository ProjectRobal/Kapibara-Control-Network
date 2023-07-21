import numpy as np

import neuron
from specie import Specie

class Layer:
    '''
        A class that defines hidden layer of network
        it has a list with references for each neuron.
    '''
    def __init__(self,input_size:int,output_size:int):
        pass


class Network:
    '''
        A class that defines network schematic.
        It stores layers wich defines hidden layers of network.
        And information of 
    '''
    def __init__(self,input_size:int,output_size:int,theta:int,tau:int):
        # a pointer to a specie network belongs to
        self.specie_ptr=None
        self.layers:list[Layer]=[]
        self.theta=theta
        self.tau=self.tau

        self.InitializeLayers()

    def InitializeLayers(self):
        pass

    def Batch(self,population:list[neuron.Neuron]):
        '''
            Take a batches from population and put them into layers.
        '''

    def Shape(self)->tuple[int,int]:
        return (self.theta,self.tau)


