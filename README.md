# physunits

Simple package with common physical unit definitions. 

## Installation

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
The unit prefixes act as simple globals. If only a set of units is desired, manually importing them as:
``from physunits import mm, nm, um``
is sufficient. 

## Contact and support
