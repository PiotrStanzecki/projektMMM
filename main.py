
import numpy as np
import control as ctrl
import matplotlib.pyplot as plt
from inputs import *

b = 0.1
k = 2
M = 1

#State space model -- 
'''
States
|x2|
|x1|

x2 - velocity
x1 - position
'''
A = np.matrix([[-b/M , -k/M],[1, 0]])
B = np.matrix([[1/M],[0]])
C1 = np.matrix([0,1]) #position output
C2 = np.matrix([1,0]) #velocity output
D = np.matrix([0])

X = np.matrix([[0],[0]])


#Simulation

deltaT = 0.01 #time step
Tend = 10 #duration of a simulation
N = int(Tend/deltaT) #number of steps
T = 3 #time period of the input
Ts = np.arange(0, N) * deltaT  # time in seconds
U = inp(Tend,T,N,"harmonic", 3, 1)
plt.plot(Ts,U)
plt.show()







