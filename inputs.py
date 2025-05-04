import numpy as np
def inp(Tend, T, N, shape, Amp):
    stepsT = N * (T/Tend) #converting time period to number of steps in simulation
    deltaY = (Amp/stepsT) #triangle function rising step
    U = [] #initializing input array
    match shape:
            case "rectangle":
                for i in range(0, N):
                    if i <= stepsT:
                        U.append(Amp)
                    else:
                        U.append(0)
            case "triangle":
                for i in range(0, N):
                    if i % stepsT == 0:
                        U.append(0)
                    else:
                        U.append(U[i - 1] + deltaY)
            case "harmonic":
                for i in range(0, N):
                    U.append(Amp*np.sin(i * 2 * np.pi / stepsT))
                   

    return U

        

















