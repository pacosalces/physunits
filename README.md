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
>>from physunits import *
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

## Description
All units are referenced to the SI. This means that base, derived, freedom (imperial), and other units including prefixes are always relative to the [SI base units](https://www.nist.gov/pml/weights-and-measures/metric-si/si-units). An example where this is manifest is that when imported, the unit ```kg``` takes on the numerical value ```1.0```, regardless of the prefix indicating the numerical factor of ```1000```.

| Unit        |    Supported    |
| :-------------: |:-------------:|
| length      | nm, um, mm, cm, m, km, inch, ft, yd |
| time      | ps, ns, us, ms, s |
| mass      | ng, ug, mg, g, kg, lb, oz |
| temperature | nK, uK, mK, K |
| angle | deg, rad, mrad |
| frequency | mHz, Hz, kHz, MHz, GHz, THz |
| voltage | pV, nV, uV, mV, V, kV |
| current | nA, uA, mA, A |
| current | nA, uA, mA, A |
| energy | mJ, J, kJ | 
| power | nW, uW, mW, W, kW, MW |
| pressure | mPa, Pa, kPa, MPa, atm, psi, Torr, mBar, Bar |
| rel concentration | ppm, ppb |

If you want a unit to be supported, feel free to open an issue.

## Contact and support
Please report, fork, test, contribute, or create an issue directly on the project's [repository](https://github.com/pacosalces/physunits).