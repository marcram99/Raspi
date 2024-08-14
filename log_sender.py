from pathlib import Path
from paramiko import SSHClient, ed25519key, AutoAddPolicy
from scp import SCPClient
from config import Config

file_name = '2024-08-06_capt01.log'
my_file = Config.files_path.joinpath(file_name)

hostname = Config.ssh_hostname
user = Config.ssh_user
ssh_key = Config.ssh_key
private_key = ed25519key.Ed25519Key.from_private_key_file(ssh_key)
with SSHClient() as client:
    client.set_missing_host_key_policy(AutoAddPolicy)
    print('---------- SSH connexion started----------')
    client.connect(hostname, username=user, pkey=private_key)
    with SCPClient(client.get_transport()) as scp:
        scp.put(my_file,'/home/ubuntu/2024-08-06_capt01.log')
print('---------- SSH connexion closed ----------')

