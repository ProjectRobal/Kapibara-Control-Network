import io
import random
import numpy as np
from BreedStrategy import BreedStrategy
import neuron

import itertools as it
import collections as ct

import more_itertools as mit

import config

from util import clip


class Block:
    def __init__(self,input_size:int,output_size:int,batch_size:int,population_size:int,strategy:BreedStrategy=BreedStrategy()) -> None:
        self.population_size=population_size

        # population size should even for crossover function
        if self.population_size%2 != 0:
            self.population_size+=1

        self.input_size=input_size
        self.output_size=output_size
        self.batch_size=batch_size

        self.number_of_breedable_neurons=0

        self.strategy=strategy

        # ratio between amount of best neurons and population size
        self.epsilon:float=1.0

        # an entire population of neurons
        self.population:list[neuron.Neuron]=[]

        # a couple of neurons picked for partipication
        self.batch:list[neuron.Neuron]=[]

    
    def getEpsilon(self)->float:
        return self.epsilon

    def updateEpsilon(self,epsilon:float):
        self.epsilon=np.clip(epsilon,0.0,1.0)
    
    def createPopulation(self):
        '''
            A function that generete initial population
        '''

        for i in range(self.population_size):
            self.population.append(neuron.Neuron(self.input_size,self.output_size))

    def PopulationSize(self)->int:
        return len(self.population)
    
    def choice(self,population:list[neuron.Neuron],batch_size:int)->list[neuron.Neuron]:
        # sort it
        population=sorted(population,key=lambda x:x.Q,reverse=True)

        batch:list[neuron.Neuron]=[]
        
        batch.extend(population[:int(self.epsilon*self.population_size)])
        
        batch.extend(random.sample(population[int(self.epsilon*self.population_size):]))

        return batch
    
    def pickBatch(self):
        '''
            A function that take random neurons from population to create batch of active neurons
        '''

        self.batch=self.choice(self.population,self.batch_size)
        #print("The best neuron Q: ",self.batch[0].Qvalue())

    def Evaluate(self,evaluation:float):
        _evaluation=evaluation/self.batch_size
        for neuron in self.batch:
            neuron.applyEvaluation(_evaluation)
            if neuron.Breedable():
                neuron.UpdateQ()
                self.number_of_breedable_neurons+=1
    
    def fire(self,inputs:np.ndarray)->np.ndarray:
        if len(inputs)!=self.input_size:
            raise ValueError("Inputs size mismatch with block input size")
        
        output=np.zeros(self.output_size,dtype=np.float32)

        for neuron in self.batch:
            output+=neuron.fire(inputs)

        return clip(output)        
    
    def ReadyForMating(self)->bool:
        return self.number_of_breedable_neurons>=self.batch_size
    
    def Mating(self)->bool:
        '''
            A function that performs crossover and mutation on population.
            A function is called when at least d members of population has performed p times.

            Apply mutation to half of population of least performing neurons and 
            couple of least peroforming neruons give random weights

        '''

        # check if population is ready
        if self.ReadyForMating():

            population=sorted(self.population,key=lambda x:x.Q,reverse=True)

            # get 50% neurons sorted by thier Q value we are extracting the best neruons here
            population=population[:int(self.population_size*0.5)]

            #print("Best neuron Q value : ",population[0].Q)

            #print("Breeding")

            self.population=[]

            self.CrossoverPopulation(population)

            for neuron in population:
                self.population.append(neuron)

            self.MutatePopulation(self.population)

            self.number_of_breedable_neurons=0

            return True
        
        return False
    
    def CrossoverPopulation(self,population):
        '''
            A function that performs crossover on neurons population.
            
        '''

        for (n1,n2) in mit.batched(population, 2):

            n1.reset()
            n2.reset()

            neuron1=self.strategy.crossover(n1,n2)
            neuron2=self.strategy.crossover(n2,n1)

            self.population.append(neuron1)
            self.population.append(neuron2)

    def MutatePopulation(self,population):
        '''
            A function that performs mutation on neurons population.
        '''

        for neuron in population:
            self.strategy.mutation(neuron)

    def save(self,memory:io.BufferedIOBase):
        '''
        Save neuron population
        Save input size
        Save output size
        Save batch size
        Save population size
        Save number_of_breedable_neurons
        '''
        metadata=np.array([self.population_size,self.input_size,self.output_size,self.batch_size,self.number_of_breedable_neurons,self.epsilon],dtype=np.int32)

        np.save(memory,metadata)

        if len(self.population)<self.population_size:
            self.population=[]
            self.createPopulation()

        for neuron in self.population:
            b_neuron:bytearray=neuron.dump()
            memory.write(b_neuron)
        
        #pkl.dump(self.strategy,memory)

    def load(self,memory:io.RawIOBase):
        metadata=np.load(memory)

        self.population_size=metadata[0]
        self.input_size=metadata[1]
        self.output_size=metadata[2]
        self.batch_size=metadata[3]
        self.number_of_breedable_neurons=metadata[4]
        self.epsilon=metadata[5]

        self.population.clear()
        self.batch.clear()

        for i in range(self.population_size):
            _neuron=neuron.Neuron(0,0)
            _neuron.load(memory)     
            self.population.append(_neuron)   
