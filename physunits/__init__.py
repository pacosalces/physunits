import numpy as np

# length
m, mm, um, nm = np.logspace(0, -9, 3)
cm = m/100

# frequency
Hz, kHz, MHz, GHz, THz = 1, 1e3, 1e6, 1e9, 1e12

# time
s, ms, us, ns, ps = 1, 1e-3, 1e-6, 1e-9, 1e-12

# power
uW, mW, W, kW = 1e-6, 1e-3, 1, 1e3

# temperature
mK, K, uK, nK = 1e-3, 1e0

# Freedom units
inch = 25.4 * mm
ft = 12 * inch