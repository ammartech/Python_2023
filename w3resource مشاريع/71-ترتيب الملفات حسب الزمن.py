import os
import datetime

def get_sorted_directory_listing(directory):
    """
    Get a sorted directory listing by creation date.
    """
    files = []
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            creation_time = os.path.getctime(file_path)
            files.append((file_name, creation_time))

    sorted_files = sorted(files, key=lambda file: file[1])
    return sorted_files

# Test the function
directory_path = "F:\باثيون"
sorted_listing = get_sorted_directory_listing(directory_path)
print("الملفات بحسب التاريخ:")
for file_name, creation_time in sorted_listing:
    formatted_time = datetime.datetime.fromtimestamp(creation_time).strftime("%a %b %d %H:%M:%S %Y")
    print(formatted_time, file_name)
