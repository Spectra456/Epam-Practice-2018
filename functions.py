import numpy as np
import math
import random

def linFunction(x, k, b):
    linFunction = np.empty(len(x))

    for i in range(linFunction.size):
        linFunction[i] = k * x[i] + b

    return (linFunction)


def sinFunction(x):
    sinFunction = np.empty(len(x))

    for i in range(sinFunction.size):
        sinFunction[i] = math.sin(x[i])

    return (sinFunction)


def logFunction(x):
    logFunction = np.empty(len(x))

    for i in range(logFunction.size):
        logFunction[i] = math.log(x[i], 2)

    return logFunction


def randFunction():
    randFunction = np.empty(random.randint(5, 100))

    for i in range(randFunction.size):
        randFunction[i] = random.random()

    return randFunction


def computeGraphs(x, k, b, s):
    if s == 1:
        return (linFunction(x, k, b))

    if s == 2:
        return (sinFunction(x))

    if s == 3:
        return (logFunction(x))

    if s == 4:
        return (randFunction())
