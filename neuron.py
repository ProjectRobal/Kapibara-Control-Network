import numpy as np

class Neuron:
    def __init__(self,input_size:int,output_size:int):
        '''
        input_size - a size of input weights
        output_size - a size of output weights

        state - a current state of a network
        past_state - a past state used in recurrent calculation
        '''
        # additional weight for past output, used for recurrsion
        # initial random weights
        self.input_weights=np.random.random(input_size+1)
        self.output_weights=np.random.random(output_size)
        self.state:float=0.0
        self.past_state:float=0.0

        # evaluation of neuron used for crossover and mutation 
        self.evaluation:float=0.0

    def reset(self):

        self.past_state=self.state
        self.state=0.0
        self.evaluation=0.0

    def setEvaluation(self,eval:float):
        self.evaluation=eval

    def getEvaluation(self)->float:
        return self.evaluation

    def Dump(self)->bytearray:
        '''
            Function used for neuron serialization,
            helpful for model saving
        '''
        pass

    def Load(self,data:bytearray):
        '''
            Function used for neuron deserialization,
            helpful for model loading
        '''
        pass        