import numpy as np
from .energy import J
from .time_units import s

# SI
nW, uW, mW, W, kW, MW = np.logspace(-9, 6, 6) * (J/s)
