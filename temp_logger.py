from datetime import datetime
from config import Config
from capteurs import Test_captor

time_stamp = f'{datetime.now():%Y-%m-%d %H:%M:%S}'
debug_logfile = Config.debug_logfile
if not debug_logfile.exists():
    debug_logfile.touch()
logfile = Config.temp_logfile
if not logfile.exists():
    logfile.touch()
temp = 0
hum = 0

data = f'{time_stamp}_T:{temp:.2f}_H:{hum:.1f}\n'
print(data)
