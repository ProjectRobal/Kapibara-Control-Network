'''
    A file that store base class for performing mutation on neurons and networks.

'''

import neuron
import network

class Mutation:
    '''
        A base class for implementing mutation method for neurons and networks.
        So each function has NotImplementedError.
    '''

    @staticmethod
    def MutateNeuron(neuron:neuron.Neuron)->neuron.Neuron:
        raise NotImplementedError()
    
    @staticmethod
    def MutateNetwork(network:network.Network)->network.Network:
        raise NotImplementedError()