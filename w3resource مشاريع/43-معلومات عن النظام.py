import platform

def os_info ():
    os_name= platform.system()
    os_platform =platform.platform()
    os_release=platform.release()
    return os_name , os_platform , os_release


os_name , os_platform , os_release= os_info()

print("نظام التشغيل", os_name)
print("المنصة", os_platform)
print("الإصدار", os_release)
