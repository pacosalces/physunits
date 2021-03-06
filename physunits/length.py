import numpy as np

# SI
km, m, mm, um, nm, pm, fm = np.logspace(3, -15, 7)
cm = m / 100

# Freedom units
inch = 25.4 * mm
ft = 12 * inch
yd = 3 * ft