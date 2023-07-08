import site

py_package = site.getsitepackages()

print("ملفات باثيون الخاصة هي:")
for index in py_package:
    print(index)
