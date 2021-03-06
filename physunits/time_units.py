import numpy as np

# SI
s, ms, us, ns, ps = np.logspace(0, -12, 5)

# Other
minute = 60 * s
hour = 60 * minute
day = 24 * hour
week = 7 * day 