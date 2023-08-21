import os
import datetime

#معلومات عن الملف

path = "F:\باثيون\w3resource مشاريع\90-copy.py"
size= os.path.getsize(path)
mode=os.stat(path).st_mode
created_time=os.path.getctime(path)
mod_time=os.path.getmtime(path)
access_time=os.path.getatime(path)

access_time = datetime.datetime.fromtimestamp(access_time)
created_time = datetime.datetime.fromtimestamp(created_time)
mod_time = datetime.datetime.fromtimestamp(mod_time)

print(path,"المسار")
print(round(size/(1024**2)),"م.ب")
print(oct(mode),"المعلومات")
print(created_time.strftime("%Y-%m-%d %H:%M:%S"))
print(mod_time.strftime("%Y-%m-%d %H:%M:%S"))
print(access_time.strftime("%Y-%m-%d %H:%M:%S"))
