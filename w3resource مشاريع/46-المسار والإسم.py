import os

current_file = os.path.abspath(__file__)
file_path=os.path.dirname(current_file)
file_name=os.path.basename(current_file)

print(f"المسار:{file_path} \n الملف:{file_name}")
