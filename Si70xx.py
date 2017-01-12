# Si70xx.py
# Copyright (c) 2017 Ben Sampson https://github.com/billyrayvalentine
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


"""
Micropython class to get data from the Silcon Labs Si70xx I2C Relative Humidity
and Temperature sensors.  It is a subclass of Si705x Temperature Sensor class

Example usage:

    from machine import Pin, I2C
    from Si70xx import Si70xx
    i2c = I2C(scl=Pin(5), sda=Pin(4))
    sensor = Si70xx(i2c)
    sensor.get_temp()

"""
from Si705x import Si705x
import time


class Si70xx(Si705x):
    """Si70xx class for Si70xx I2C Relative Humidity and Temperature sensors

    Args:
        i2c: A configured machine.I2C instance
        address: Si70xx address.  Defaults to 0x40

    """

    def __init__(self, i2c, address=0x40):
        """Inherit the Si705x Class as this only adds get_humidity()"""
        super().__init__(i2c, address)

        self._humidity_code = bytearray(2)

    def get_humidity(self, delay=20):
        """Return humidity percentage

        Args:
            delay: Time in ms to wait for sensor to take a measurement
        """

        buf = bytearray(2)

        self._i2c.writeto(self.address, b'\xF5')
        time.sleep_ms(delay)
        self._i2c.readfrom_into(self.address, buf)

        # Keep temp in object for potential debug
        self._humidity_code = buf[0] << 8 | buf[1]

        return self._humidity_code * 125 / 65536 - 6
