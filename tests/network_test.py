import numpy as np

import network
import neuron
import activation

import timeit


# in Kapibara I am going to parse sensor data of about 587 elements
neurons:list[neuron.Neuron]=[neuron.Neuron(587,activation=activation.relu.Relu)]*2048

network=network.Network(587,1,1,128,587)

input=np.random.random(587)

print("Inputs:",input)

network.Batch(neurons)

print(len(neurons))

start=timeit.default_timer()

out=network.Forward(input)

print("time: ",timeit.default_timer()-start, " s")

print(out)