import numpy as np

import neuron
import network
from base.crossover import Crossover

class OnePoint(Crossover):
    '''
        A base class for implementing crossover method for neurons and networks.
        So each function has NotImplementedError.
    '''
    @staticmethod
    def cross_numpy(x1:np.array,x2:np.array)->np.array:
        output=np.ndarray(len(x1),np.float32)

        output[0:len(x1)/2]=x2[0:len(x1)/2]
        output[(len(x1)/2)+1:len(x1)]=x1[(len(x1)/2)+1:len(x1)]

        return output
        

    @staticmethod
    def CrossNeurons(neuron1:neuron.Neuron,neuron2:neuron.Neuron)->neuron.Neuron:
        out=neuron.Neuron(neuron1.input_size(),neuron1.output_size())

        out.input_weights=Flip.cross_numpy(neuron1.input_weights,neuron2.input_weights)
        out.output_weights=Flip.cross_numpy(neuron1.output_weights,neuron2.output_weights)

        return out
    
    @staticmethod
    def CrossNetworks(network1:network.Network,network2:network.Network)->network.Network:
        raise NotImplementedError()