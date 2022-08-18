import json
from datetime import datetime
from pathlib import Path

from config import Config

print('LIGHT LOGGER')
log_file = Config.light_logfile
data_file = Config.data_file
if not data_file.exists():
    with open(data_file,'w') as new_file:
        json.dumps({'light_mode':'dark',
                    'change_time':'',
                    'mail_time': '',
                    'mail_alert':0
                    },new_file)
print(data_file)
with open(data_file) as json_file:
    data = json.load(json_file)
