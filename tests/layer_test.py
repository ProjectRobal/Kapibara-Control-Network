import numpy as np
import layer
import math

import timeit

'''

Now we have problem with nan value.


'''

# readings from sensors plus compressed audio spectogram, outputs: motor output power and three action (froward,backward,stop)
layer1=layer.Layer(6,256,8,64,512)

layer2=layer.Layer(256,2,4,64,512)

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

    return np.exp(-np.abs(e)*0.001)*100.0

for n in range(1000000):
    #start=timeit.default_timer()

    output=layer2.fire(layer1.fire(inputs))

    error=regression_test(output[0],output[1])

    eval=error_to_rewrd(error)

    print("Output reward",eval)

    layer1.evalute(eval/2.0)
    layer2.evalute(eval/2.0)

    layer2.mate()
    layer1.mate()

    #print("Time: ",timeit.default_timer()-start," s")
