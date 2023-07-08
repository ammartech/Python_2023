import os
entry = 'A1.py'

def check_for_the_entry (entry):
    if os.path.isdir(entry):
        print("إنه مسار")
    elif os.path.isfile (entry):
        print("إنه ملف")
    else:
        print("لربما شئ آخر")

check_for_the_entry (entry)

