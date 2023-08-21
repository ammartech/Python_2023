import subprocess

return_afte_exec = subprocess.check_output("dir", shell=True , universal_newlines=True)

print (return_afte_exec)
