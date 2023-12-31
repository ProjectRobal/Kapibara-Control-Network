'''
    A file that store some generall configuration of environment.

'''

from dotproducts.dotnumpy import NumpyDotProduct


# percentage of best neuron to keep in population without any crossover
BEST_NEURONS=0.25

MIN_EPSILON=0.0

# percentage of least performed neurons in block that will be mutated
LEAST_NEURONS_K=0.8

# a precentage number of amount of population that took required number of actions in block, required for mating to occur
MATING_TRESHOLD=0.25

# a number of trials nueron has to take before mating
NUMBER_OF_TRIALS=5

# a factor that control evaluation process 
LEARING_RATE=0.8

# a number in second, after which network will be reseted when no new minima has been found
STALL_TIME=2.5*60

# a dot product a method that will be used in program

DOT_PRODUCT=NumpyDotProduct

# some constrains that prevent nan or inf to occur

MAX_VALUE_NUMBER=10000000.0

MIN_VALUE_NUMBER=-10000000.0


