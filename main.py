
import numpy as np
import matplotlib.pyplot as plt
from inputs import *
from output import *


b = 1
k = 1
M = 1

#State space model -- 
'''
States
|x2|
|x1|

x2 - velocity
x1 - position
'''
A = np.array([[-b/M , -k/M],[1, 0]])
B = np.array([[1/M],[0]])
C1 = np.array([0,1]) #position output
C2 = np.array([1,0]) #velocity output
D = np.array([0])



#Simulation

deltaT = 0.001 #time step
Tend = 30 #duration of a simulation
N = int(Tend/deltaT) #number of steps
T = 3 #time period of the input
Ts = np.arange(0, N) * deltaT  # time in seconds

#input
U = inp(Tend,T,N,"triangle", 4, 1)



# Initial state
X = np.array([[0],[0]])

(yx1,yv1) = euler(A,B,U,X,deltaT,N)
(yx2,yv2) = rung(A,B,U,X,deltaT,N)

# Plot
plt.figure(1)
plt.subplot(211)
plt.plot(Ts, yx1, label="Position")
plt.plot(Ts, yv1, label="velocity")
plt.plot(Ts, U, label="Input", linestyle='--')
plt.title("Euler")
plt.legend()
plt.grid(True)


plt.subplot(212)
plt.plot(Ts, yx2, label="Position")
plt.plot(Ts, yv2, label="velocity")
plt.plot(Ts, U, label="Input", linestyle='--')
plt.xlabel("Time (s)")
plt.title("Runge-Kutta")
plt.legend()
plt.grid(True)
plt.show()






