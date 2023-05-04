from pathlib import Path
from paramiko import SSHClient, ed25519key, AutoAddPolicy
from config import Config

ssh_key = Config.ssh_key
private_key = ed25519key.Ed25519Key.from_private_key_file(ssh_key)
client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy)
cmd = 'ls -l'
print('---------- start SSH connexion----------')
client.connect('46.226.104.139', username='ubuntu', pkey=private_key)
sftp_client = client.open_sftp()
# sftp_client.get(remote_path, output_file)
# sftp_client.put(local_path, remote_path)
client.close()
print('---------- SSH connexion closed ----------')

"""
stdin, stdout, stderr = client.exec_command(cmd)
output = stdout.read()
print(str(output, 'utf8'))

log_path = Path.home().joinpath('Raspi/logfiles')
content = list(log_path.glob('*.log'))
print(content)
print(20*'-')
print(f'nb de fichier:{len(content)}')
"""
