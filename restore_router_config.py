from netmiko import ConnectHandler

R1 = {
     'device_type': 'cisco_ios',
     'ip': '192.168.1.1',
     'username': 'admin',
     'password': 'pass123',
     'secret': 'pass123'
}
backup_file = input("Enter the name of the backup file to restore: ")

with open(backup_file, 'r') as file:
	backup_config = file.read()

net_connect = ConnectHandler(**R1)

net_connect.enable()
net_connect.config_mode()
output = net_connect.send_command_timing(backup_config)

net_connect.exit_config_mode()

net_connect.disconnect()
