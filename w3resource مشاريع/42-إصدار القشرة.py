import platform

def check_py_shell():
    if platform.architecture()[0]=='32bit':
        return "32-Bit"
    elif platform.architecture()[0]=='64bit':
        return "64-Bit"
    else:
        return "Unknown"

py_mode= check_py_shell()

print("إصدار القشرة هي:", py_mode)
