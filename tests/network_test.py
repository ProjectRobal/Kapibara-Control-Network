import numpy as np

import network
import neuron
import activation

import timeit


neurons:list[neuron.Neuron]=[neuron.Neuron(32,activation=activation.relu.Relu)]*256

network=network.Network(4,1,1,32)

input=np.random.random(4)

print("Inputs:",input)

network.Batch(neurons)

print(len(neurons))

start=timeit.default_timer()

out=network.Forward(input)

print("time: ",timeit.default_timer()-start, " s")

print(out)