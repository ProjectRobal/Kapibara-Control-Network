'''
    A file that store base class for performing crossover between nuerons and networks schematics.

'''

import neuron
import network

class Crossover:
    '''
        A base class for implementing crossover method for neurons and networks.
        So each function has NotImplementedError.
    '''

    @staticmethod
    def CrossNeurons(neuron1:neuron.Neuron,neuron2:neuron.Neuron)->neuron.Neuron:
        raise NotImplementedError()
    
    @staticmethod
    def CrossNetworks(network1:network.Network,network2:network.Network)->network.Network:
        raise NotImplementedError()