from base.mutation import Mutation

import numpy as np

import neuron
import network

class GaussMutaion(Mutation):
    '''
        A base class for implementing mutation method for neurons and networks.
        So each function has NotImplementedError.
    '''

    @staticmethod
    def MutateNeuron(neuron:neuron.Neuron)->neuron.Neuron:

        neuron.input_weights+=np.random.normal(size=len(neuron.input_weights))
        neuron.output_weights+=np.random.normal(size=len(neuron.output_weights))

        return neuron
    
    @staticmethod
    def MutateNetwork(network:network.Network)->network.Network:
        raise NotImplementedError()