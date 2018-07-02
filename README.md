import matplotlib.pyplot as plt
import numpy as np
import math
import random

x = [1,2,3,4,5,6,7,8]

class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))

def linFuction(x, k, b):

    linFunction = np.empty(10)

    for i in range(linFunction.size):

        linFunction[i] = k * x[i] + b

    return(linFuction)

def sinFuction(x):

    sinFunction = np.empty(10)

    for i in range(sinFunction.size):

        sinFunction[i] = math.sin(x[i]);

    return (sinFuction)

def logFunction(x):

    logFunction = np.empty(10)

    for i in range(logFunction.size):

        logFunction[i] = math.log(x[i], 2)

    return (logFunction)

def randFuction():

    randFuction = np.empty(10)

    for i in range(randFuction.size):

        randFuction[i] = random.random();

    return randFuction

def computeGraphs(x,k,b,s):

  while switch(s):

     if case(1):

       linFuction(x, k, b)

     if case(2):

       sinFuction(x)

     if case(3):

       logFunction(x)

     if case(4):

       randFuction()



plt.plot(randFuction()),antialiased=True,linestyle = "-",color = "b")
plt.grid(True)
plt.show()