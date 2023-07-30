import random
import numpy as np
from BreedStrategy import BreedStrategy
import neuron

import itertools as it
import collections as ct

import more_itertools as mit

import config


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

        # an entire population of neurons
        self.population:list[neuron.Neuron]=[]

        # a couple of neurons picked for partipication
        self.batch:list[neuron.Neuron]=[]

    
    def createPopulation(self):
        '''
            A function that generete initial population
        '''

        for i in range(self.population_size):
            self.population.append(neuron.Neuron(self.input_size,self.output_size))

    def PopulationSize(self)->int:
        return len(self.population)
    
    def pickBatch(self):
        '''
            A function that take random neurons from population to create batch of active neurons
        '''
        self.batch=random.sample(self.population,self.batch_size)

    def Evaluate(self,evaluation:float):
        _evaluation=evaluation/self.batch_size
        for neuron in self.batch:
            neuron.applyEvaluation(_evaluation)
            if neuron.Breedable():
                self.number_of_breedable_neurons+=1
    
    def fire(self,inputs:np.ndarray)->np.ndarray:
        if len(inputs)!=self.input_size:
            raise ValueError("Inputs size mismatch with block input size")
        
        output=np.zeros(self.output_size,dtype=np.float32)

        for neuron in self.batch:
            output+=neuron.fire(inputs)

        return output        
    
    def Mating(self):
        '''
            A function that performs crossover and mutation on population.
            A function is called when at least d members of population has performed p times.

            Apply mutation to half of population of least performing neurons and 
            couple of least peroforming neruons give random weights

        '''

        # check if population is ready
        if self.number_of_breedable_neurons>=self.population_size:

            population=sorted(self.population,key=lambda x:x.evaluation,reverse=True)

            population=population[:int(self.population_size*0.5)]

            print("Best neuron eval: ",population[0].evaluation)

            print("Breeding")

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

    def Save(self):
        pass

    def Load(self):
        pass