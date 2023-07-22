import numpy as np

import neuron
from specie import Specie

class Layer:
    '''
        A class that defines hidden layer of network
        it has a list with references for each neuron.
    '''
    def __init__(self,input_size:int,output_size:int):
        self.neuron_batch_size=output_size

    def size(self)->int:
        return self.neuron_batch_size
    



class Network:
    '''
        A class that defines network schematic.
        It stores layers wich defines hidden layers of network.
        And information of 
    '''
    def __init__(self,input_size:int,output_size:int,theta:int,tau:int):
        self.input_size=input_size
        self.output_size=output_size
        
        # a pointer to a specie network belongs to
        self.specie_ptr=None
        self.theta=theta
        self.tau=self.tau

        if self.theta<=0:
            self.theta=1
        if self.tau<=0:
            self.tau=1

        # for now we use only one leayer
        self.theta=1
        
        self.InitializeLayers()

    def InitializeLayers(self):
        '''
         For now we will use only one layer for simplicity
        '''
        self.layers:list[Layer]=[Layer(self.input_size,self.output_size)]*self.theta

    def Batch(self,population:list[neuron.Neuron]):
        '''
            Take a batches from population and put them into layers.
        '''

    def Shape(self)->tuple[int,int]:
        return (self.theta,self.tau)


