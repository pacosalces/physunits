# physunits

Simple package with common physical unit definitions. 

## Installation
Add this package to your existing python environment with pip
```pip install physunits```, or alternatively follow your distribution specific instructions. 

## Usage
An example usage of this package is:
```python
>> from physunits import *
>> print(f"{1000 * cm / um:.2f} is how many microns there are in a thousand centimeters")
10000000.00 is how many microns there are in a thousand centimeters
```

The package tries to include only the most used unit prefixes, but you can generate other units, for example:
```python
>> from physunits import *
>> minute = 60 * s
>> hour = 60 * minute
>> day = 24 * hour
>> print(f'There are approximately {365*day / hour} hours in a year.')
There are approximately 8760.0 hours in a year.
```
The unit prefixes act as simple globals. If only a subset of the supported units is desired, manually importing them as

```python
from physunits import mm, nm, um
```
is good enough. 

Another example where physunits may be useful is illustrated by the following script dealing with a voltage trace:
```python
import numpy as np
import matplotlib.pyplot as plt
from physunits import *

f = 2.12*kHz
omega = 2*np.pi*f
t = np.linspace(-670*us, 410*us, 2**10)
my_voltage = (1.5*mV) * np.sin(omega*t)

# Now plot voltage in mV vs time in ms
plt.plot(t/ms, my_voltage/mV)
plt.xlabel(r't (ms)')
plt.ylabel(r'V (mV)')
plt.show()
```
which outputs the following plot:
![example_plot](/docs/readme_plot.png)

## Description
All units are referenced to the SI. This means that base, derived, freedom (imperial), and other units including prefixes are always relative to the [SI base units](https://www.nist.gov/pml/weights-and-measures/metric-si/si-units). An example where this is manifest is that when imported, the unit ```kg``` takes on the numerical value ```1.0```, regardless of the prefix indicating the numerical factor of ```1000```.

| Unit        |    Supported    |
| :-------------: |:-------------:|
| length | fm, pm, nm, um, mm, cm, m, km, inch, ft, yd |
| time | ps, ns, us, ms, s |
| mass | ng, ug, mg, g, kg, lb, oz |
| temperature | nK, uK, mK, K |
| angle* | deg, rad, mrad |
| frequency | mHz, Hz, kHz, MHz, GHz, THz |
| voltage | pV, nV, uV, mV, V, kV |
| charge | C, mC, uC, nC |
| current | nA, uA, mA, A |
| resistance | Ohm, mOhm, kOhm, MOhm, GOhm |
| capacitance | F, mF, uF, nF, pF | 
| inductance | H, mH, uH, nH |
| magnetic field strength| T, mT, uT, nT, pT | 
| energy** | mJ, J, kJ, meV, eV, keV, MeV, GeV, TeV | 
| power | nW, uW, mW, W, kW, MW |
| pressure | mPa, Pa, kPa, MPa, atm, psi, Torr, mBar, Bar |
| rel concentration | ppm, ppb |

If you want a unit to be supported, feel free to open an issue.

* We _all_ know that if there was an SI unit for angles, it would be the radian, so in ```physunits```, it takes the value ```rad = 1.0 ```, and degrees are defined relative to it. This works nicely in all trig functions. Special thanks to chrisjbillington for pointing this out.

** While the electronvolt (```eV```) is not a part of the SI, the SI [recognizes its use](https://en.wikipedia.org/wiki/Non-SI_units_mentioned_in_the_SI). Furthermore, the [latest SI redefinition](https://en.wikipedia.org/wiki/2019_redefinition_of_the_SI_base_units) fixed the value of the electron charge constant, effectively fixing the conversion between ```eV``` and ```J```.

## Contact and support
Please report, fork, test, contribute, or create an issue directly on the project's [repository](https://github.com/pacosalces/physunits).