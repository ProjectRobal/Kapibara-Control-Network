# Kapibara Control Network

## Introduction:

 A neuroevolution algorithm to control my social robot called Kapibara. 
It is based or inspired by neuroevolution algorithm such as:
- NEAT - a network wich can adjust it's size
- SANE - a network wich evolve neurons rather than entire network
- ESP - a SANE but with recurrent neurons
- CCMA - a algorithm wich utilize couple of cooperating networks 
- ECNN - a network wich not only return action to take but also estimation of quality of action

## Assumptions:

1. Algorithm uses population of neurons as genes. Every neuron has input, output weights. Since it is a neuroevolution algorithm it isn't vulnerable for gradient explosion or vanishing gradient so it is able to use plain recurrent connection.

1. Instead of crossing / mutate entiere networks we are going to apply evolution on neurons population. ( like in ESP )

1. Every layer is composed from blocks, each block acts like sub network with it's own neuron population from which couple of neurons are picked to form sub network.

1. At every step, block picks neurons at random. Then network is evaluated. Evaluation score is evenly distributed to each block.
Block is going to keep copy of best sub network.

1. When k neurons participated in n steps, mating in block occurs, where block perform crossover and mutation on it's neuron population plus it's best sub network to keep stability in evaluation score.

1. In addition the epsilon variable is introduced. It is ratio between 0.0 to 1.0 which decide what precentage of neurons in sub population comes from best sub network. The idea is when we are satisfied with network score we can set epsilon to 1.0 and call it a day. It can be useful in real time environment.


## File description:

- neuron.py - store class that defines neuron object
- network.py - store class related to network and network template
- crossover.py - holds base class for neurons and networks crossover
- mutation.py - holds base class for neuron and network mutation
- dotproduct.py - holds base class for dot product calculation used by neurons
