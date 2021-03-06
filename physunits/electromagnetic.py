import numpy as np

# SI for all, no exception

# current
nA, uA, mA, A = np.logspace(-9, 0, 4)

# voltage
pV, nV, uV, mV, V, kV = np.logspace(-12, 3, 6)

# electric charge 
C, mC, uC, nC = np.logspace(0, -9, 4)

# electric resistance
mOhm, Ohm, kOhm, MOhm, GOhm = np.logspace(-3, 9, 5)

# electric capacitance
pF, nF, uF, mF, F = np.logspace(-12, 0, 5)

# electric inductance
nH, uH, mH, H = np.logspace(-9, 0, 4)

# magnetic field
pT, nT, uT, mT, T = np.logspace(-12, 0, 5)