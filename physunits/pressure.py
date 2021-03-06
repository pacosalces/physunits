import numpy as np
from .mass import kg
from .length import m
from .time_units import s

# SI
mPa, Pa, kPa, MPa = np.logspace(-3, 6, 4) * (kg / m / s**2)

# Freedom units
psi = 6894.757293168*Pa

# Other
atm = 101325*Pa
Torr = 1 / (760*atm)
Bar, mBar = 1e-5*Pa, 1e-5*mPa