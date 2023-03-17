import subprocess

cmd = ['vcgencmd','measure_te mp']
proc = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
o,e = proc.communicate()

print(o.decode('ascii'))

