import numpy as np
import matplotlib.pyplot as plt
import layer
import network
from BreedStrategy import BreedStrategy
import math

import timeit

import sys, os
import datetime

from crossover.qonepoint import QOnePoint


'''

Now we have problem with nan value which is solve yeah!

I need to think about a way to favorize the best network configuration.
Because we are getting bunch of networks that are meah and then we got one 
the best of the bounch.
I think to store N best networks and when we get apropiete amount of networks
perform crossover over thier populations.

When we increase block number and decrese neuron number in each, the network comes 
to best solution faster.

By looking at the reward plot I see the problem. It is really unstable between high reward
steps are deep deepresions.
We need to think about some method that will make reward more stable.
For optimalizations problems were we find best networks work given problem 
it is quite good, but we need something that is more stable.

By running network couple of times it seems that rewards collection become more dense.
But still we want something more stable.
We can put Q for every neurons and pick neurons with biggest Q.

Or we can keep copy of best network and inject neurons from best network into current network.

I would try with the first proposition.

 With Q valued neurons network coverage to best solution much faster and the reward distribution across
steps seems to be more even. But using weighted methods of getting batch of neurons seems to slow down 
inner working of network.

 I think I have found an issue, the ouputs are always at thier limits. I need to find out why?  
 
 What I can consider:

 -Input and output normalization

 -Other weights intialization random distribution

 -When network doesn't progress for long time reinitialize population

'''

last_eval:float=0

epsilon=0.0

def trendfunction(eval:float,network:network.Network)->float:
    global epsilon

    if eval==0:
        return epsilon

    if eval>last_eval:
        epsilon+=1.0
    
    return epsilon
    
# readings from sensors plus compressed audio spectogram, outputs: motor output power and three action (froward,backward,stop)
breed_str=BreedStrategy()
breed_str.cross=QOnePoint

network1=network.Network(6,breed_str)

network1.addLayer(256,32)
network1.addLayer(2,16)

if os.path.exists("tests/checkpoint/last.chk"):
    print("Loading checkpoint!!")
    network1=network.NetworkParser.load("tests/checkpoint/last.chk")

network1.setTrendFunction(trendfunction)

# linear regression problem

points=[(-1.0,1.0),(-0.73,1.54),(-0.43,2.14)]

inputs=np.array([-1.0,1.0,-0.73,1.54,-0.43,2.14],dtype=np.float32)

def regression_test(a:float,b:float)->float:
    error:float=0.0

    for x,y in points:
        _y=a*x+b
        error+=(y-_y)**2
    
    return error

def error_to_rewrd(e:float)->float:

    return np.exp(-np.abs(e)*0.01)*100.0

x=[]

best_val=0

for n in range(2000):
    start=timeit.default_timer()

    output=network1.step(inputs/1.0)

    error=regression_test(output[0]*1.0,output[1]*1.0)

    eval=error_to_rewrd(error)

    x.append(eval)

    network1.evalute(eval)

    last_eval=eval

    if eval>best_val:
        best_val=eval
        print("Best reward after: ",n," steps")
        print(eval)
        network.NetworkParser.save(network1,"tests/checkpoint/best.chk")
    else:
        print("Time: ",timeit.default_timer()-start," s")

    #print("Output reward",eval)



plt.figure()
network.NetworkParser.save(network1,"tests/checkpoint/last.chk")
plt.plot(range(len(x)),x)
print("Reward variance: ",np.var(x))
plt.savefig("tests/imgs/figure"+str(datetime.datetime.now())+".png")

plt.show()
