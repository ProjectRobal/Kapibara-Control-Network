import numpy as np
import random

import neuron

class Layer:
    '''
        A class that defines hidden layer of network
        it has a list with references for each neuron.
    '''
    def __init__(self,input_size:int,batch_size:int):
        '''
            input_size - a layer input size
            batch_size - a number of neurons utilized by layer
        '''
        self.input_size=input_size
        self.neuron_batch_size=batch_size
        self.neuron_batch=[]

    def batch(self,neurons:list[neuron.Neuron]):
        '''
            Sample random neurons into layer
        '''
        self.neuron_batch=random.sample(neurons,self.neuron_batch_size)

    def forward(self,inputs:np.array)->np.ndarray:
        '''
            A function that calculate output of layer, based 
            on inputs
        '''
        output=np.ndarray(self.neuron_batch_size,dtype=np.float32)
        i:int=0

        for neur in self.neuron_batch:
            
            output[i]=neur.fire(inputs)
            i+=1

        return output

    def backward(self,evaluation:float):
        '''
            Function that pass evaluation value to each neurons evenly
        '''
        eval:float=evaluation/self.neuron_batch_size

        for neuron in self.neuron_bacth:
            neuron.applyEvaluation(eval)


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


