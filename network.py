import numpy as np
import random

from base.activation import Activation
from base.dotproduct import Product
from activation.linear import Linear
from dotproducts.dotnumpy import NumpyDotProduct
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

    def batch(self,neurons:list[neuron.Neuron])->list[neuron.Neuron]:
        '''
            Sample random neurons into layer
        '''
        self.neuron_batch=random.sample(neurons,self.neuron_batch_size)

        return self.neuron_batch

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
        And information of number of layers and total count of neurons.
        Each layer will have neuron count equal to tau.
    '''
    def __init__(self,input_size:int,output_size:int,theta:int,tau:int,dotproduct:Product=NumpyDotProduct):
        '''
            theta - number of layers
            tau - number of neuron population
        '''
        self.dot_product=dotproduct

        self.input_size=input_size
        self.output_size=output_size
        self.theta=theta
        self.tau=self.tau

        if self.theta<=0:
            self.theta=1
        if self.tau<=0:
            self.tau=1

        # for now we use only one leayer
        self.theta=1

        # Q estimation output
        self.outpu_layer:list[neuron.Neuron]=[neuron.Neuron(self.tau,Linear,dotproduct)]
        
        self.InitializeLayers()

    def InitializeLayers(self):
        '''
         For now we will use only one layer for simplicity
        '''
        self.layers:list[Layer]=[Layer(self.input_size,self.tau)]*self.theta

    def addOutputNode(self,activation:Activation):
        
        self.outpu_layer.append(neuron.Neuron(self.layers[-1].neuron_batch_size,activation,self.dot_product))

    def Batch(self,population:list[neuron.Neuron])->list[neuron.Neuron]:
        '''
            Take a batches from population and put them into layers.
        '''
        neuron_pool:list[neuron.Neuron]=random.sample(population,self.tau)

        for layer in self.layers:
            taken:list[neuron.Neuron]=layer.batch(neuron_pool)

            # remove a choosen neurons from current pool
            neuron_pool.remove(taken)

    def Forward(self,inputs:np.ndarray)->np.ndarray:
        layer_out=inputs
        for layer in self.layers:
            layer_out:np.ndarray=layer.forward(layer_out)


        output:np.ndarray=np.zeros(len(self.outpu_layer),dtype=np.float32)


        for out_neuron,out in zip(self.outpu_layer,output):
            out=out_neuron.fire(layer_out)

        return output

    def Shape(self)->tuple[int,int]:
        return (self.theta,self.tau*self.theta)


