import numpy as np

import network
import neuron
import activation

import timeit


neurons:list[neuron.Neuron]=[neuron.Neuron(4,activation=activation.relu.Relu)]*256

layer1=network.Layer(4,32)

layer1.batch(neurons)

input=np.random.random(4)

print("Inputs:",input)

start=timeit.default_timer()

out=layer1.forward(input)

print("time: ",timeit.default_timer()-start, " s")

print(out)