import numpy as np
import io

import config

from util import clip


class Neuron:
    def __init__(self,input_size:int,output_size:int):
        '''
        input_size - a size of input weights
        output_size - a size of output weights

        state - a current state of a network
        '''
        # additional weight for past output, used for recurrsion
        # initial random weights
        self.input_weights=(np.random.random(input_size)-0.5)*10
        self.output_weights=(np.random.random(output_size)-0.5)*10
        self.state:float=0.0
        self.dot_product=config.DOT_PRODUCT
        # count in how many trials neuron has particpated
        self.trails=0

        # evaluation of neuron used for crossover and mutation 
        self.evaluation:float=0.0

    def fire(self,inputs:np.ndarray)->np.ndarray:

        self.state=self.dot_product(self.input_weights,inputs)

        return clip(self.output_weights*self.state)


    def input_size(self)->int:
        return len(self.input_weights)
    
    def output_size(self)->int:
        return len(self.output_weights)

    def reset(self):

        self.state=0.0
        self.evaluation=0.0
        self.trails=0.0

    def reinitialize(self):
        self.input_weights=(np.random.random(self.input_size())-0.5)
        self.output_weights=(np.random.random(self.output_size())-0.5)

    def setEvaluation(self,eval:float):
        self.evaluation=eval

    def applyEvaluation(self,eval:float):
        self.evaluation+=eval
        self.trails+=1

    def getEvaluation(self)->float:
        return self.evaluation
    
    def Breedable(self)->bool:
        '''
            Whether the neuron is ready for breeding
        '''
        if self.trails>=config.NUMBER_OF_TRIALS:
            self.trails=0
            return True
        
        return False

    def dump(self)->bytearray:
        '''
            Function used for neuron serialization,
            helpful for model saving
            Save inputs weights
            Save outputs weights
            Save trails numbers
        '''
        input_neurons=io.BytesIO()
        output_neurons=io.BytesIO()
        metadata=io.BytesIO()

        neuron_metadata=np.array([self.trails],dtype=np.int32)

        np.save(metadata,neuron_metadata)
        np.save(input_neurons,self.input_weights)
        np.save(output_neurons,self.output_weights)

        metadata=metadata.getvalue()
        input_neurons=input_neurons.getvalue()
        output_neurons=output_neurons.getvalue()

        output=bytearray(metadata)
        output.extend(input_neurons)
        output.extend(output_neurons)

        return output

    def load(self,data:bytearray|io.BytesIO):
        '''
            Function used for neuron deserialization,
            helpful for model loading
        '''
        if type(data) is bytearray:
            inputs=io.BytesIO(data)
        else:
            inputs=data

        metadata=np.load(inputs)
        input_neurons=np.load(inputs)
        output_neurons=np.load(inputs)

        self.trails=metadata[0]

        self.input_weights=input_neurons
        self.output_weights=output_neurons

    def __str__(self) -> str:
        return "Inputs: "+str(self.input_weights)+"\n"+"Outputs: "+str(self.output_weights)