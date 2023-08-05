'''
    A file that store some generall configuration of environment.

'''

from dotproducts.dotnumpy import NumpyDotProduct


# percentage of best neuron to keep in population without any crossover
BEST_NEURONS=0.05

# percentage of least performed neurons in block that will be mutated
LEAST_NEURONS_K=0.6

# percentage of least peroformed neurons in block that will lost and replaced by new ones
NUERONS_TO_REMOVE=0.25

# a precentage number of amount of population that took required number of actions in block, required for mating to occur
MATING_TRESHOLD=0.9

# a number of trials nueron has to take before mating
NUMBER_OF_TRIALS=5

# a dot product a method that will be used in program

DOT_PRODUCT=NumpyDotProduct

# some constrains that prevent nan or inf to occur

MAX_VALUE_NUMBER=1000.0

MIN_VALUE_NUMBER=-1000.0
