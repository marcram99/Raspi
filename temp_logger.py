from datetime import datetime
from config import Config
from capteurs import Temp_captor

time_stamp = f'{datetime.now():%Y-%m-%d %H:%M:%S}'
debug_logfile = Config.debug_logfile
if not debug_logfile.exists():
    debug_logfile.touch()
logfile = Config.temp_logfile
if not logfile.exists():
    logfile.touch()

t_capt = Temp_captor()
temp = t_capt.read_temp()
hum = t_capt.read_hum()
data = f'{time_stamp}_T:{temp:.2f}_H:{hum:.1f}\n'

with open(logfile,'a') as log:
    log.write(data)
