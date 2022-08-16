from datetime import datetime, timedelta
from pathlib import Path

#configuration des différents chemins d'accès des logfiles
class Config():
    logfiles_path = Path.home().joinpath('Raspi/logfiles')
    if not logfiles_path.exists():
        Path.mkdir(logfiles_path)

    light_logfile = logfiles_path.joinpath(f'{datetime.now():%Y-%m}_capt02.log')
    temp_logfile = logfiles_path.joinpath(f'{datetime.now():%Y-%m-%d}_capt01.log')    
    debug_logfile = logfiles_path.joinpath('00_DEBUG_logfile.log')
    data_file = Path.home().joinpath('Raspi/data.json')

