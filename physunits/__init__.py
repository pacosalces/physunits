import numpy as np

 ## ##     ####
##   ##     ##
####        ##
 #####      ##
    ###     ##
##   ##     ##
 ## ##     ####

# length
km, m, mm, um, nm = np.logspace(3, -9, 5)
cm = m/100

# angle (technically not SI... why not? because politics?)
mrad, rad = np.logspace(-3, 0, 2)
deg = np.pi * rad / 180

# mass (note the SI convention for base unit)
ng, ug, mg, g, kg, = np.logspace(-9, 0, 5)

# frequency
mHz, Hz, kHz, MHz, GHz, THz = np.logspace(-3, 12, 6)

# time
s, ms, us, ns, ps = np.logspace(0, -12, 5)

# temperature
nK, uK, mK, K = np.logspace(-9, 0, 4)

# current
nA, uA, mA, A = np.logspace(-9, 0, 4)

# voltage
pV, nV, uV, mV, V, kV = np.logspace(-12, 3, 6)

# charge 
C, mC, uC, nC = np.logspace(0, -9, 4)

# energy
mJ, J, kJ = np.logspace(-3, 3, 3) * (kg * m**2 / s**2)
eV = 1.602176634e-19 * C
meV = 1e-3 * eV
keV, MeV, GeV, TeV = np.logspace(3, 12, 4)

# power
nW, uW, mW, W, kW, MW = np.logspace(-9, 6, 6) * (J/s)

# pressure
mPa, Pa, kPa, MPa = np.logspace(-3, 6, 4) * (kg / m / s**2)

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

# mass
lb = 0.45359237*kg
oz = lb / 16

# pressure
psi = 6894.757293168*Pa

 ## ##   #### ##  ###  ##  ### ###  ### ##
##   ##  # ## ##   ##  ##   ##  ##   ##  ##
##   ##    ##      ##  ##   ##       ##  ##
##   ##    ##      ## ###   ## ##    ## ##
##   ##    ##      ##  ##   ##       ## ##
##   ##    ##      ##  ##   ##  ##   ##  ##
 ## ##    ####    ###  ##  ### ###  #### ##

# relative concentration
ppm, ppb = 1e-6, 1e-9

# pressure
atm = 101325*Pa
Torr = 1 / (760*atm)
Bar, mBar = 1e-5*Pa, 1e-5*mPa