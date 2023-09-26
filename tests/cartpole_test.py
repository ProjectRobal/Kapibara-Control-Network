import os
import numpy as np
import gymnasium

from network import Network,NetworkParser
from layer import RecurrentLayer
from BreedStrategy import BreedStrategy

from activation.sigmoid import Sigmoid
from initializer.gaussinit import GaussInit

from buffer import TrendBuffer

import matplotlib.pyplot as pyplot

env=gymnasium.make("CartPole-v1",render_mode="human")

init=GaussInit(0,0.01)

network1=Network(2)

network1.addLayer(2,8,RecurrentLayer,[Sigmoid,Sigmoid],init)

evaluation_trend:TrendBuffer=TrendBuffer(20)

epsilon=0.4

trends:float=[]

def trendfunction(eval:float,network:Network)->float:

    trend:float=evaluation_trend.trendline()
    trends.append(trend)
    global epsilon

    evaluation_trend.push(eval)

    print("Trend: ",trend)

    if eval>40:
        epsilon=1.0
 
    return epsilon


def state_to_reward(observation:np.ndarray):
    p=observation[0]
    theta=observation[2]
    return  - (p**2)/11.52 - (theta**2)/288

if os.path.exists("tests/checkpoint/last.pk"):
    print("Loading checkpoint!!")
    #It doesn't load for some reason
    #network1=NetworkParser.load("tests/checkpoint/last.pk")

network1.setTrendFunction(trendfunction)


(state,_) = env.reset()

EPISODE_NUMBER=1000

rewards=[]

action=0

inputs:np.ndarray=np.array([state[0],state[2]])

episode=0

best_score=0

while True:
    
    env.render()

    terminated=False

    steps=0

    while not terminated:

        action:int=np.argmax(network1.step([state[0],state[2]]))

        state,reward,terminated,truncated,info=env.step(action)

        steps+=1

    print("Episode: ",episode, "finished with ",steps," steps")

    (state,_)=env.reset()

    rewards.append(steps)

    network1.evalute(steps)
    print("Reward: ",steps)
    print("Epsilon: ",network1.layers[0].blocks[0].epsilon)

    #if steps > best_score:
    #    best_score=steps
    NetworkParser.save(network1,"tests/checkpoint/last.pk")

    episode+=1

env.close()

pyplot.plot(np.arange(0,EPISODE_NUMBER,1),rewards)

pyplot.show()