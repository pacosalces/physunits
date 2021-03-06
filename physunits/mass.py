import numpy as np

# Note the SI convention for base unit, kg = 1.0
ng, ug, mg, g, kg, = np.logspace(-12, 0, 5)

# Freedom units
lb = 0.45359237 * kg
oz = lb / 16
