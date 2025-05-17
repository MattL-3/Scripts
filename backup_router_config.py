from netmiko import ConnectHandler

R1 = {
     'device_type': 'cisco_ios',
     'ip': '192.168.1.1',
     'username': 'admin',
     'password': 'pass123',
     'secret': 'pass123'
}

net_connect = ConnectHandler(**R1)

net_connect.enable()
hostname = net_connect.send_command('show running-config | i hostname')
hostname = hostname.split()[-1]
output = net_connect.send_command('show running-config')

filename = f"{hostname}_config_backup.txt"
with open(filename, 'w') as file:
	file.write(output)

print(f"{hostname} configuration is saved to {filename}")

net_connect.disconnect()
