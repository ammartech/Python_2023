import subprocess

# تنفيذ الأمر
command = "dir"
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# الطباعة
print(result.stdout)
