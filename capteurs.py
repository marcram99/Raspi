from datetime import datetime
from config import Config

time_stamp = f'{datetime.now():%Y-%m-%d %H:%M:%S}'
debug_logfile = Config.debug_logfile
if not debug_logfile.exists():
    debug_logfile.touch()
logfile = Config.temp_logfile
if not logfile.exists():
    logfile.touch()


class Temp_captor():
    import board
    import busio
    import adafruit_si7021

    def __init__(self):
        self.i2c = self.busio.I2C(self.board.SCL, self.board.SDA)
        bad_captor = 1
        counter = 0
        while bad_captor:
            try:
                self.sensor = self.adafruit_si7021.SI7021(self.i2c)
                bad_captor = 0
            except RuntimeError:
                bad_captor = 1
                counter += 1
            else:
                with open(debug_logfile, 'a') as f:
                    f.write(f'{time_stamp} DEBUG: Capteur init après {counter + 1} essais\n')

    def read_all(self):
        bad_read = 1
        while bad_read:
            try:
                temp = self.sensor.temperature
                hum = self.sensor.relative_humidity
                bad_read = 0
            except Exception:
                bad_read = 1
        return {'température': temp, 'humidité': hum}

    def read_temp(self):
        bad_read = 1
        while bad_read:
            try:
                temp = self.sensor.temperature
                bad_read = 0
            except Exception:
                bad_read = 1
        return temp

    def read_hum(self):
        bad_read = 1
        while bad_read:
            try:
                hum = self.sensor.relative_humidity
                bad_read = 0
            except Exception:
                bad_read = 1
        return hum


class Light_captor():
    import board
    import busio
    import adafruit_tsl2591

    def __init__(self):
        self.i2c = self.busio.I2C(self.board.SCL, self.board.SDA)
        self.sensor = self.adafruit_tsl2591.TSL2591(self.i2c)

    def read_ir(self):
        return self.sensor.infrared

    def read_lux(self):
        return self.sensor.lux

    def read_all(self):
        lux = self.sensor.lux
        ir = self.sensor.infrared
        return {'lux': lux, 'ir': ir}

    def read_state(self, seuil_nuit):
        """Renvoi la valeur 'light' ou 'dark'
        en fonction du param:'seuil nuit'"""
        if self.sensor.lux > seuil_nuit:
            return "light"
        else:
            return "dark"
