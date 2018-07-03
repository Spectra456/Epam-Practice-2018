import matplotlib.pyplot as plt
import functions as f

# Input

print("Please choose type of function\n"
      "1 - Linear\n"
      "2 - Sinus\n"
      "3 - Log\n"
      "4 - Random\n")
s = int(input())
a = [0, 0]
c = 0
d = 0

if s == 1 or s == 2 or s == 3:
  print("Please, enter x array")
  a = list(map(int, input().split()))
  if s == 1:
      print("Please, enter additional arguments k and b for linear function")
      c= int(input())
      d= int(input())





def computeGraphs(x,k,b,s):

     if s==1:
         return (f.linFunction(x, k, b))


     if s==2:
         return (f.sinFunction(x))

     if s==3:
         return (f.logFunction(x))

     if s==4:
         return (f.randFunction())



plt.plot(computeGraphs(a,c,d,s),antialiased=True,linestyle = "-",color = "b")
plt.show()