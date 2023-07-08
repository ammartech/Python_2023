import os

def check_file_exist(file_name):
    return os.path.isfile(file_name)

file_name = input("أدخل مسار الملف")

if check_file_exist(file_name):
    print("الملف موجود")
else:
    print("المف غير موجود")
