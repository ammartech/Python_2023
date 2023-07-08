import os

def list_files_in_dic(dictionary):
    files_dic =os.listdir(dictionary)
    for file_n in files_dic:
        if os.path.isfile(os.path.join(dictionary, file_n)):
            print(file_n)


dic_path='H:\Websites'

list_files_in_dic(dic_path)
        
