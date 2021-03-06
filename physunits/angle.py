import numpy as np

# Technically not SI... why not?! #makeradiansanSIunit
mrad, rad = np.logspace(-3, 0, 2)
deg = np.pi * rad / 180