from pathlib import Path

log_path = Path.home().joinpath('Raspi/logfiles')
content = list(log_path.glob('*.log'))
print(content)
