from datetime import datetime, timedelta
from pathlib import Path

# configuration des différents chemins d'accès des logfiles


class Config():
    # macbook path:
    files_path = Path.home().joinpath('Documents/code/python/Raspi/files')
    logfiles_path = Path.home().joinpath('Documents/code/python/Raspi/logfiles')
    ssh_key = Path.home().joinpath('.ssh/id_ed25519')
    # mac path:
    #files_path = Path.home().joinpath('Marc-perso/code/python/Raspi/files')
    #logfiles_path = Path.home().joinpath('Marc-perso/code/python/Raspi/logfiles')
    # linux path:
    #files_path = Path.home().joinpath('Raspi/files')
    #logfiles_path = Path.home().joinpath('Raspi/logfiles')
    if not files_path.exists():
        Path.mkdir(files_path)
    if not logfiles_path.exists():
        Path.mkdir(logfiles_path)
    light_logfile = logfiles_path.joinpath(f'{datetime.now():%Y-%m}_capt02.log')
    temp_logfile = logfiles_path.joinpath(f'{datetime.now():%Y-%m-%d}_capt01.log')
    debug_logfile = logfiles_path.joinpath('00_DEBUG_logfile.log')
  
    data_file = files_path.joinpath('data.json')
    test_lightcaptor = files_path.joinpath('light.json')

    light_mode = 'dark'
