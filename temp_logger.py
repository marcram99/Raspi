#! /usr/bin/python3.5
# encoding:utf-8
import digitalio
import board
import busio
import adafruit_si7021
import adafruit_tsl2591

from pathlib import Path
from datetime import datetime
from config import Config

time_stamp = f'{datetime.now():%Y-%m-%d %H:%M:%S}'
debug_logfile = Config.debug_logfile
if not debug_logfile.exists():
    debug_logfile.touch()
logfile = Config.temp_logfile
if not logfile.exists():
    logfile.touch()

i2c = busio.I2C(board.SCL, board.SDA)
bad_captor = 1
bad_read = 1
counter = 0
while bad_captor:
    try:
        sensor01 = adafruit_si7021.SI7021(i2c)
        bad_captor = 0
    except RuntimeError:
        bad_captor = 1
        counter += 1
    else:
        with open(debug_logfile, 'a') as f:
            f.write(f'{time_stamp} DEBUG: Capteur init après {counter + 1} essais\n')
        count = 0
        while bad_read or (count > 9):
            try:
                temp = sensor01.temperature
                hum = sensor01.relative_humidity 
                data = f'{time_stamp}_T:{temp:.2f}_H:{hum:.1f}({count + 1})\n'
                bad_read = 0
            except Exception as e:
                bad_read = 1
                count += 1
            else:
                with open(logfile, 'a') as f:
                    f.write(data)
        if bad_read:
            with open(debug_logfile, 'a') as f:
                f.write(f'{time_stamp} DEBUG:échec après {count} essais \n')
