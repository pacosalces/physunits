import numpy as np

 ## ##     ####
##   ##     ##
####        ##
 #####      ##
    ###     ##
##   ##     ##
 ## ##     ####

##  ###  ###  ##    ####  #### ##   ## ##
##   ##    ## ##     ##   # ## ##  ##   ##
##   ##   # ## #     ##     ##     ####
##   ##   ## ##      ##     ##      #####
##   ##   ##  ##     ##     ##         ###
##   ##   ##  ##     ##     ##     ##   ##
 ## ##   ###  ##    ####   ####     ## ##


# length
km, m, mm, um, nm = np.logspace(3, -9, 5)
cm = m/100

# mass (notice the SI convention for the base unit)
ng, ug, mg, g, kg, = np.logspace(-6, 1, 5)

# frequency
mHz, Hz, kHz, MHz, GHz, THz = np.logspace(-3, 12, 6)

# time
s, ms, us, ns, ps = np.logspace(0, -12, 5)

# power
nW, uW, mW, W, kW, MW = np.logspace(-9, 6, 6)

# temperature
nK, uK, mK, K = np.logspace(-3, 0, 4)

# current
nA, uA, mA, A = np.logspace(-9, 0, 4)

# voltage
pV, nV, uV, mV, V, kV = np.logspace(-12, 3, 6)

# energy
mJ, J, kJ = np.logspace(-3, 3, 3)

### ###  ### ##   ### ###  ### ###  ### ##    ## ##   ##   ##
 ##  ##   ##  ##   ##  ##   ##  ##   ##  ##  ##   ##   ## ##
 ##       ##  ##   ##       ##       ##  ##  ##   ##  # ### #
 ## ##    ## ##    ## ##    ## ##    ##  ##  ##   ##  ## # ##
 ##       ## ##    ##       ##       ##  ##  ##   ##  ##   ##
 ##       ##  ##   ##  ##   ##  ##   ##  ##  ##   ##  ##   ##
####     #### ##  ### ###  ### ###  ### ##    ## ##   ##   ##


##  ###  ###  ##    ####  #### ##   ## ##
##   ##    ## ##     ##   # ## ##  ##   ##
##   ##   # ## #     ##     ##     ####
##   ##   ## ##      ##     ##      #####
##   ##   ##  ##     ##     ##         ###
##   ##   ##  ##     ##     ##     ##   ##
 ## ##   ###  ##    ####   ####     ## ##

# length
inch = 25.4 * mm
ft = 12 * inch
yd = 3 * ft

# power
