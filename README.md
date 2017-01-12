README.md
# micropython-Si70xx
A MicroPython library for the I2C [Silicon Labs Si70xx](http://www.silabs.com/products/sensors/humidity-sensors/Pages/default.aspx) series of relative humidity and temperature sensors.  
This library should work with the Si7006 Si7013 Si7020 Si7021 Si7034

This class is a subclass of the [billyrayvalentine/micropython-Si705x] (https://github.com/billyrayvalentine/micropython-Si705x) and must therefor be available to Micropython.

**This module has currently only been tested on the Si7021.  Please report your milage**

# Methods
There are only four methods:

```get_temperature``` - Perform a measurement and return the temperature in Celsius

```get_humidity``` - Perform a measurement and return the relative humidity percentage

```get_model``` - Return the hardware model e.g. Si7021

```get_firmware_version``` - Return the hex value of the firmware version

# Example in REPL
```python
>>> from machine import Pin, I2C
>>> from Si70xx import Si70xx
>>> i2c = I2C(scl=Pin(5), sda=Pin(4))
>>> sensor = Si70xx(i2c)
>>> sensor.get_temperature()
23.64604
>>> sensor.get_humidity()
41.74857
>>> sensor.get_model()
'Si7021'
>>> sensor.get_firmware_version()
'0x20'

```

# License
MIT
