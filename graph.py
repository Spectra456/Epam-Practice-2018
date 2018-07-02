import matplotlib.pyplot as plt
import numpy as np
import math
import random

#Input

print("Please choose type of function\n"
      "1 - Linear\n"
      "2 - Sinus\n"
      "3 - Log\n"
      "4 - Random\n")
a = [0,0]
c = 0
d = 0
s = int(input())

if s == 1 or s == 2 or s == 3:
  print("Please, enter x array")
  a = list(map(int, input().split()))
  if s == 1:
      print("Please, enter additional arguments k and b for linear function")
      c= int(input())
      d= int(input())



def linFunction(x,k,b):

    linFunction = np.empty(len(a))

    for i in range(linFunction.size):

        linFunction[i] = k * x[i] + b

    return(linFunction)

def sinFunction(x):

    sinFunction = np.empty(len(a))

    for i in range(sinFunction.size):

        sinFunction[i] = math.sin(x[i]);

    return (sinFunction)

def logFunction(x):

    logFunction = np.empty(len(a))

    for i in range(logFunction.size):

        logFunction[i] = math.log(x[i], 2)

    return (logFunction)

def randFunction():

    randFunction = np.empty(random.randint(5,100))

    for i in range(randFunction.size):

        randFunction[i] = random.random();

    return randFunction

def computeGraphs(x,k,b,s):

     if s==1:

       return(linFunction(x,k,b))


     if s==2:

       return(sinFunction(x))

     if s==3:

       return(logFunction(x))

     if s==4:

       return(randFunction())



plt.plot(computeGraphs(a,c,d,s),antialiased=True,linestyle = "-",color = "b")
plt.grid(True)
plt.savefig("rand")
plt.show()