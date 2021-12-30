import subprocess
sub = subprocess.Popen("echo Hello World", shell=True, stdout=subprocess.PIPE)
subprocess_return = sub.stdout.read()
print(subprocess_return)