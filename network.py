import numpy as np
import numpy.ma as ma
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
        Layer has mask used when number of inputs isn't equal to neuron weight size thanks to
        that it only used couple of neurons.
    '''
    def __init__(self,input_size:int,batch_size:int,max_synaps_size:int):
        '''
            input_size - a layer input size
            batch_size - a number of neurons utilized by layer
        '''
        self.input_size=input_size
        self.mask=[0]*input_size

        choose_mask=random.sample(range(max_synaps_size),input_size)

        i:int=0
        for choosen in choose_mask:
            self.mask[i]=choosen
            i+=1

        print(self.mask)

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
            
            output[i]=neur.fire(inputs,self.mask)
            i+=1

        return output

    def backward(self,evaluation:float):
        '''
            Function that pass evaluation value to each neurons evenly
        '''
        eval:float=evaluation/self.neuron_batch_size

        for neuron in self.neuron_batch:
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
    def __init__(self,input_size:int,output_size:int,theta:int,tau:int,max_neuron_weight_size:int,dotproduct:Product=NumpyDotProduct):
        '''
            theta - number of layers
            tau - number of neuron population
        '''
        self.max_neuron_weight_size=max_neuron_weight_size
        self.dot_product=dotproduct

        self.input_size=input_size

        self.theta=theta
        self.tau=tau

        if self.theta<=0:
            self.theta=1
        if self.tau<=0:
            self.tau=1

        # for now we use only one layer
        #self.theta=1

        self.InitializeLayers()

        self.layers.append(Layer(self.tau,output_size+1,max_neuron_weight_size))

        self.output_activation_function:list[Activation]=[Linear]*(output_size+1)

    def InitializeLayers(self):
        '''
         For now we will use only one layer for simplicity
        '''
        self.layers:list[Layer]=[Layer(self.input_size,self.tau,self.max_neuron_weight_size)]

        for i in range(self.theta-1):
            self.layers.append(Layer(self.tau,self.tau,self.max_neuron_weight_size))

    def setActivationFunction(self,id:int,activation:Activation):
        if id>=len(self.output_activation_function):
            return
        
        self.output_activation_function[id]=activation

    def getNeuronCount(self)->int:
        output:int=0

        for layer in self.layers:
            output+=layer.neuron_batch_size

        return output

    def Batch(self,population:list[neuron.Neuron])->list[neuron.Neuron]:
        '''
            Take a batches from population and put them into layers.
        '''
        neuron_pool:list[neuron.Neuron]=random.sample(population,self.getNeuronCount())
        print(len(neuron_pool))

        for layer in self.layers:
            taken:list[neuron.Neuron]=layer.batch(neuron_pool)

            # remove a choosen neurons from current pool
            for x in taken:
                neuron_pool.remove(x)

    def Forward(self,inputs:np.ndarray)->np.ndarray:
        layer_out=inputs
        for layer in self.layers:
            layer_out:np.ndarray=layer.forward(layer_out)

        return layer_out

    def Shape(self)->tuple[int,int]:
        return (self.theta,self.tau*self.theta)


