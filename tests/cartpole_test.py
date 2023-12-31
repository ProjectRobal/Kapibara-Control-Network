import os
import numpy as np
import gymnasium

from network import Network,NetworkParser
from layer import RecurrentLayer,Layer
from BreedStrategy import BreedStrategy

from activation.sigmoid import Sigmoid
from activation.linear import Linear
from activation.relu import Relu
from initializer.gaussinit import GaussInit

from buffer import TrendBuffer

import matplotlib.pyplot as pyplot

env=gymnasium.make("CartPole-v1",render_mode="human")

init=GaussInit(0,1.0)

network1=Network(4)

network1.addLayer(2,4,Layer,[Relu,Relu],init,(8,64))

evaluation_trend:TrendBuffer=TrendBuffer(20)

epsilon=0.0

trends:float=[]

best_eval=0

def trendfunction(eval:float,network:Network)->float:

    trend:float=evaluation_trend.trendline()
    global epsilon
    global best_eval

    #print("Trend: ",trend)

    evaluation_trend.push(eval)

    if eval>best_eval:
        best_eval=eval
        print("New best score: ",best_eval)

    #_epsilon=np.exp(2.3*(eval/500))*0.1

    _epsilon=eval/2000

    if _epsilon>epsilon:
        epsilon=_epsilon
 
    return epsilon

if os.path.exists("tests/checkpoint/last.pk"):
    print("Loading checkpoint!!")
    #It doesn't load for some reason
    network1=NetworkParser.load("tests/checkpoint/last.pk")

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

    steps_list:list[float]=[]

    #network1.shuttle()

    for i in range(1):

        steps=0

        network1.shuttle()

        while not terminated:
            output=network1.run(state)
            action:int=np.argmax(output)

            state,reward,terminated,truncated,info=env.step(action)

            steps+=1

            if steps>2000:
                terminated=True

        terminated=False
        (state,_)=env.reset()
        
        #network1.evalute(steps)
        steps_list.append(steps)
        network1.evalute(steps)

    evaluation=np.mean(steps_list)

    steps_list.clear()

    rewards.append(evaluation)
    
    NetworkParser.save(network1,"tests/checkpoint/last.pk")

    episode+=1

env.close()

pyplot.plot(np.arange(0,EPISODE_NUMBER,1),rewards)

pyplot.show()