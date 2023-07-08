filename =input("أدخل اسم الملف")
n = filename.find(".")
extension = filename[n+1::]
print("الصيغة", extension)
