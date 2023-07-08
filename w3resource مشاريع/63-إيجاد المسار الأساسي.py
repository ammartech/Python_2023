import os

file_path= input("أدخل المسار المطلوب")

abs_path=os.path.abspath(file_path)


print(abs_path)
