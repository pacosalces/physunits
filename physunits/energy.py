import numpy as np
from .mass import kg
from .length import m
from .time_units import s
from .electromagnetic import C

# SI
mJ, J, kJ = np.logspace(-3, 3, 3) * (kg * m**2 / s**2)
eV = 1.602176634e-19 * C
meV = 1e-3 * eV
keV, MeV, GeV, TeV = np.logspace(3, 12, 4)