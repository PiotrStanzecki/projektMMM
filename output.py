import numpy as np

def euler(A,B,U,X,deltaT,N):
    yx = []
    yv = []

    # Simulation loop
    for i in range(N):
        dX = A @ X + B * U[i]
        X = X + deltaT * dX
        yx.append(X[1,0])
        yv.append(X[0,0])

    # Convert y to flat array
    yx = np.array(yx).flatten()
    yv = np.array(yv).flatten()

    return (yx,yv)

def rung(A,B,U,X,deltaT,N):
    yx = []
    yv = []

    # Simulation loop
    #f(U,X)
    for i in range(N):
        k1 = deltaT * (A @ X + B * U[i])
        k2 = deltaT * (A @ ( X + k1/2) + B * (U[i] + deltaT/2))
        k3 = deltaT * (A @ ( X + k2/2) + B * (U[i] + deltaT/2))
        k4 = deltaT * (A @ ( X + k3) + B * (U[i] + deltaT))
        dX = (1/6)*(k1 + 2 * k2 + 2 * k3 + k4)
        X = X + dX

        yx.append(X[1,0])
        yv.append(X[0,0])

    # Convert y to flat array
    yx = np.array(yx).flatten()
    yv = np.array(yv).flatten()

    return (yx,yv)
