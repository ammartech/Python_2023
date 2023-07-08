import os

path = os.environ['PATH']
paths_list = path.split(os.pathsep)
formatted_path = '\n'.join(paths_list)
print(formatted_path)


