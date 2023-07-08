import os
import datetime

path_entry= input("أدخل المسار المطلوب")

creation_time= os.path.getctime(path_entry)
creation_datetime= datetime.datetime.fromtimestamp(creation_time)

modification_time= os.path.getmtime(path_entry)
modification_datetime=datetime.datetime.fromtimestamp(modification_time)


print(creation_datetime)
print(modification_datetime)
