import numpy as np
import matplotlib.pyplot as plt
from inputs import *  
from output import *   

def simulate_system(b, k, M, deltaT, Tend, T, shape, Amp):
    #state-space
    A = np.array([[-b / M, -k / M],[1, 0]])
    B = np.array([[1 / M],[0]])
    C1 = np.array([0, 1])  # position output
    C2 = np.array([1, 0])  # velocity output
    D = np.array([0])

  
    N = int(Tend / deltaT)
    Ts = np.arange(0, N) * deltaT  # time vector

    #Input 
    U = inp(Tend, T, N, shape, Amp)

    
    X = np.array([[0],[0]])

    #Simulations
    yx1, yv1 = euler(A, B, U, X, deltaT, N)
    yx2, yv2 = rung(A, B, U, X, deltaT, N)

    #Plotting
    plt.figure(1)
    plt.clf()

    plt.subplot(311)
    plt.plot(Ts, yx1, label="Position")
    plt.plot(Ts, yv1, label="Velocity")
    plt.plot(Ts, U, label="Input", linestyle='--')
    plt.title("Euler Method")
    plt.legend()
    plt.grid(True)

    plt.subplot(312)
    plt.plot(Ts, yx2, label="Position")
    plt.plot(Ts, yv2, label="Velocity")
    plt.plot(Ts, U, label="Input", linestyle='--')
    plt.title("Runge-Kutta Method")
    plt.legend()
    plt.grid(True)

    plt.subplot(313)
    plt.plot(Ts, yx2 - yx1, label="Position")
    plt.plot(Ts, yv2 - yv1, label="Velocity")
    plt.xlabel("Time (s)")
    plt.title("Difference")
    plt.legend()
    plt.grid(True)
    plt.show()
